# Intstacull

Tags: python, web
Tech: selenium

## Dependencies

- Python > 3
- Selenium and the chrome web driver

## Run

1. Create a file called [config.py](http://config.py) that contains the following variables with your login credentials

   ```python
   username = 'your_username'
   password = 'your_password'
   ```

2. Execute [main.py](http://main.py) and watch selenium work its magic.

   ```bash
   python main.py
   ```

## Notes

- Thanks to [https://github.com/aj-4](https://github.com/aj-4) for the original work - Instagram has since changed its front-end.
- If you have two-factor auth enabled this probably won't work.
