import sqlite3

conn = sqlite3.connect('exchange.sqlite') 
result = conn.execute("""
    SELECT COUNT(DISTINCT ge.receiver_id)
    FROM gift_exchanges ge
    JOIN user_wishlists uw
    ON ge.receiver_id = uw.user_id AND ge.gift_name = uw.gift_name;
""").fetchone()
print(f'gifts: {result[0]}')
conn.close()
