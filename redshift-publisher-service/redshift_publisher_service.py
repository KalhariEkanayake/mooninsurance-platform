import psycopg2
import redshift_connector
import os

def sync_to_redshift():
    try:
        print("Connecting to Postgres...")
        pg_conn = psycopg2.connect(
            host=os.getenv("PG_HOST"),
            dbname=os.getenv("PG_DB"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD")
        )
        pg_cur = pg_conn.cursor()
        pg_cur.execute("SELECT * FROM your_table ORDER BY created_at DESC LIMIT 1")
        row = pg_cur.fetchone()

        if not row:
            print("No data to sync.")
            return

        print("Connecting to Redshift...")
        rs_conn = redshift_connector.connect(
            host=os.getenv("REDSHIFT_HOST"),
            database=os.getenv("REDSHIFT_DB"),
            user=os.getenv("REDSHIFT_USER"),
            password=os.getenv("REDSHIFT_PASSWORD")
        )
        rs_cur = rs_conn.cursor()

        # Update with your actual columns
        rs_cur.execute("""
            INSERT INTO your_redshift_table (col1, col2, col3)
            VALUES (%s, %s, %s)
        """, row)
        rs_conn.commit()

        print("✅ Sync successful!")
    except Exception as e:
        print("❌ Sync failed:", str(e))
        raise

if __name__ == "__main__":
    sync_to_redshift()
