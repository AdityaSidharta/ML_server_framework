from src.utils.envs import titanic_filename, postgres_ipaddress, postgres_password, postgres_port, postgres_username
from src.utils.io import read_data, write_db, create_db_connection


def setup_db():
    connection = create_db_connection(postgres_username, postgres_password, postgres_ipaddress, postgres_port)
    df_full = read_data(titanic_filename)
    write_db(df_full, titanic_filename, connection)


if __name__ == '__main__':
    setup_db()
