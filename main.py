from google.transit import gtfs_realtime_pb2
import requests

def fetch_transit_data():
    feed_url = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw'
    print(f"Connecting to transit stream...")

    try:
        response = requests.get(feed_url, timeout=10)
        response.raise_for_status()

        feed = gtfs_realtime_pb2.FeedMessage()

        feed.ParseFromString(response.content)

        print("\n--- Live Data Success ---")
        for i, entity in enumerate(feed.entity):
            if i >= 10: 
                break
            print(f"\nEntity #{i+1}:")
            print(entity)

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == '__main__':
    fetch_transit_data()