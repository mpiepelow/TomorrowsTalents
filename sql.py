# Fill in credentials
host='#####'
port='####'
database='postgres'
user='maximilianpiepelow'
password='#####'


from sqlalchemy import create_engine    
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

# Import the Python packages for get_data() function



# Insert the get_data() function definition below
