# CurrencyExchangeRateChecker

**Currency Exchange Rate Checker - Usage Guide**

1. **Prerequisites**:
   - Python installed on your system.
   - The `requests` library installed. You can install it using `pip install requests` if it's not already installed.

2. **Download the Script**:
   - You can download the script from the following link: [CurrencyExchangeRateChecker.py](https://raw.githubusercontent.com/YuanLiuchang/CurrencyExchangeRateChecker/main/CurrencyExchangeRateChecker.py). Save it to your local directory.

3. **Run the Script**:
   - Open your command prompt or terminal.
   - Navigate to the directory where you saved the script using the `cd` command.
   - Run the script using the following command:
     ```
     python CurrencyExchangeRateChecker.py
     ```

4. **API Key Setup**:
   - You will be prompted to enter API keys. Enter each API key and press `Enter`.
   - To finish setting up API keys, type 'q' and press `Enter`.

5. **API URL**:
   - You will be prompted to enter the API URL. You can either press `Enter` to use the default URL (https://open.er-api.com/v6/latest/) or provide your custom URL.

6. **Currency Selection**:
   - Enter the base currency code when prompted (e.g., USD, EUR, GBP) and press `Enter`.
   - Enter the target currency code (e.g., USD, EUR, GBP) and press `Enter`.

7. **Observe Exchange Rates**:
   - The script will start fetching exchange rates using the provided API keys and show the conversion rate from the base currency to the target currency.
   - It will automatically update the rates every 30 minutes.

8. **Exit the Program**:
   - To stop the script, you can press `Ctrl + C` in the terminal.

That's it! You now have a Currency Exchange Rate Checker that can monitor exchange rates using different APIs and update the rates every 30 minutes. Enjoy using the tool for currency exchange rate analysis.
