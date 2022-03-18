from supertokens_python import init, InputAppInfo, SupertokensConfig ,get_all_cors_headers
from supertokens_python.recipe import passwordless, session
from supertokens_python.recipe.passwordless import ContactEmailOnlyConfig, CreateAndSendCustomEmailParameters
from typing import Union, Dict, Any
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.framework.fastapi import Middleware

async def send_email(
    param: CreateAndSendCustomEmailParameters,
    user_context: Dict[str, Any]
):
    # send the email to this email ID
    email = param.email,
    print(email)

    # this is the OTP string. It will be defined if the flowType
    # is "USER_INPUT_CODE_AND_MAGIC_LINK" or "USER_INPUT_CODE"
    user_input_code: Union[str, None] = param.user_input_code
    print(user_input_code)

    # this is the magic link string. It will be defined if the flowType
    # is "USER_INPUT_CODE_AND_MAGIC_LINK" or "MAGIC_LINK"
    url_with_link_code: Union[str, None] = param.url_with_link_code
    print(url_with_link_code)

    # This is the time in milliseconds for how long the url_with_link_code or user_input_code is valid for. */
    code_life_time = param.code_life_time,
    print(code_life_time)

    # pre_auth_session_id can be used for advanced customizations that need to
    # fetch data from the database or access something saved earlier in the process. */
    pre_auth_session_id: str = param.pre_auth_session_id
    print(pre_auth_session_id)

    # TODO: send SMS...
    return None

init(
    app_info=InputAppInfo(
        app_name="fastapi-react",
        api_domain="http://localhost:8000",
        website_domain="http://localhost:3000",
        api_base_path="/auth",
        website_base_path="/auth"
    ),
    supertokens_config=SupertokensConfig(
        # These are the connection details of the app you created on supertokens.com
        connection_uri="https://47e56b41a6e211ec86997d1f55128682-us-east-1.aws.supertokens.io:3569",
        api_key="5=uH64YiEGnEAQ7Wdo4BEKcmSc9Wr5"
    ),
    framework='fastapi',
    recipe_list=[
        session.init(), # initializes session features
        passwordless.init(
            flow_type="USER_INPUT_CODE",
            contact_config=ContactEmailOnlyConfig(
                create_and_send_custom_email=send_email
            )
        )
    ],
    mode='asgi' # use wsgi if you are running using gunicorn
)

app = FastAPI()
app.add_middleware(Middleware)

# TODO: Add APIs

app = CORSMiddleware(
    app=app,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)