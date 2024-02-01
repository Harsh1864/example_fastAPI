import time
from plyer import notification

def water_reminder():
    while True:
        # Remind every 1 hour (3600 seconds) or adjust the time as needed
        time.sleep(2)
        notification.notify(
            
            title='Hydration Reminder',
            message='It\'s time to drink water!',
            app_name='Water Reminder',
            timeout=1  # Notification will disappear after 10 seconds
        )

if __name__ == "__main__":
    water_reminder()
