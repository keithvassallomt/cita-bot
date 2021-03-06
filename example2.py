# import os

from bcncita import CustomerProfile, DocType, Office, OperationType, Province, try_cita

if __name__ == "__main__":
    customer = CustomerProfile(
        anticaptcha_api_key="... your key here ...",
        anticaptcha_plugin_path="/Users/username/Downloads/anticaptcha-plugin_v0.50.crx",
        auto_captcha=True,
        auto_office=True,
        chrome_driver_path="/usr/local/bin/chromedriver",
        # chrome_profile_name="Profile 7",
        # chrome_profile_path=f"{os.curdir}/chrome_profiles/",
        save_artifacts=True,
        telegram_token="... your key here ...",
        # wait_exact_time = [
        #     [0, 0], # [minute, second]
        #     [15, 0],
        #     [30, 0],
        #     [45, 0],
        # ],
        province=Province.BARCELONA,
        operation_code=OperationType.TOMA_HUELLAS,
        doc_type=DocType.PASSPORT,
        doc_value="1100123123",
        country="RUSIA",
        name="BORIS JOHNSON",
        phone="600000000",
        email="myemail@here.com",
        offices=[
            Office.BARCELONA,
            Office.MATARO,
        ],
    )
    try_cita(context=customer, cycles=100)
