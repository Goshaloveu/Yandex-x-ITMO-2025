import sqlite3
import pandas as pd

db_path = "space-example.sqlite" 
planet   = "Дна Гуранд"
capacity = 2
distance = 8

sql = """
with 
my_planet as (
    select
        id as planet_id,
        star_id,
        `name` as planet_name
    from
        planets p
    where
        p.name = $planet
),
products_on_start as (
    select
        product_type,
        buy_price,
        sell_price,
        amount,
        pt.name as product_type_name,
        mp.planet_id,
        mp.star_id,
        mp.planet_name
    from
        prices pr
    inner join
        my_planet mp on pr.planet_id = mp.planet_id
    left join
        product_types pt on pr.product_type = pt.id
),
systems as (
    select distinct
        sm.star_from_id as from_star_id,
        sm.star_to_id as dest_star_id,
        sm.distance as dist
    from
        star_map sm
    inner join
        my_planet as mp on sm.star_from_id = mp.star_id
    where
        sm.distance <= $distance
        and sm.star_to_id != mp.star_id
),
dest_planets as (
    select
        pl.id as planet_id,
        pl.name as planet_name,
        sys.from_star_id as from_star_id,
        sys.dest_star_id as star_id,
        s.name as dest_star_name,
        sys.dist as dist,
        pr.product_type as product_id,
        pr.buy_price,
        pr.sell_price,
        pr.amount
    from
        systems as sys
    inner join
        planets pl on sys.dest_star_id = pl.star_id
    inner join
        prices pr on pl.id = pr.planet_id
    inner join
        stars as s on sys.dest_star_id = s.id
)
select
    dp.planet_name as planet_name,
    dp.dest_star_name as star_name,
    pos.product_type_name as product_name,
    case when $capacity < pos.amount then $capacity else pos.amount end as amount_to_buy,
    (case when $capacity < pos.amount then $capacity else pos.amount end) * (dp.sell_price - pos.buy_price) as profit
from
    dest_planets dp
inner join
    products_on_start pos
on
    dp.product_id = pos.product_type
where
    profit > 0
order by
    profit desc,
    planet_name asc,
    product_name asc
limit
    10
;
"""

with sqlite3.connect(db_path) as conn:
    df = pd.read_sql_query(sql, conn, params={
        "planet":   planet,
        "capacity": capacity,
        "distance": distance
    })

# Вывод результата
print(df)
