import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile, HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models

def ask_chatglm(prompt, secret_id, secret_key, model="chatglm3-6b"):
    try:
        cred = credential.Credential(secret_id, secret_key)

        httpProfile = HttpProfile()
        httpProfile.endpoint = "hunyuan.tencentcloudapi.com"  # 正确 Endpoint

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile

        # region 留空或用空字符串 ""
        client = hunyuan_client.HunyuanClient(cred, "", clientProfile)

        req = models.ChatStdRequest()
        params = {
            "Model": model,
            "Messages": [{"Role": "user", "Content": prompt}],
        }
        req.from_json_string(json.dumps(params))

        resp = client.ChatStd(req)
        return resp.Choices[0].Message.Content

    except TencentCloudSDKException as err:
        return f"调用失败: {err}"
