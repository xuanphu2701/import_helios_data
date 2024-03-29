# Selenium Import Helios Data
## Prerequisite
### Install Tesseract
- Install Tesseract: https://github.com/UB-Mannheim/tesseract/wiki
- Install it (avoid Installing in *Program Files* directory)
- Change BYTETESSERACT_LOCAL_PATH in extract_capcha.py to your tesseract.exe path
### Chrome driver
- Download chrome driver here: https://googlechromelabs.github.io/chrome-for-testing/#stable
- Or download chrome driver for Window x64: https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.86/win64/chromedriver-win64.zip
- Change CHROME_DRIVER_PATH in main.py to your chrome driver path

## Image pool
 - You can add image to the pool by copy it to ./img/img_pool directory
 - Then run change_img_name.py 
