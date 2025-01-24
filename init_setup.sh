echo [%date% %time%]: START

echo [%date% %time%]: creating env with python 3.8 version

python -m venv env

echo [%date% %time%]: activating the environment

.\env\Scripts\activate

echo [%date% %time%]: installing the dev requirements

pip install -r requirements_dev.txt

echo [%date% %time%]: END
