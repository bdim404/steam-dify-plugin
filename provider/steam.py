from typing import Any
import requests

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class SteamProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            # 获取API Key
            api_key = credentials.get("api_key")
            if not api_key:
                raise ToolProviderCredentialValidationError("Steam API Key不能为空")
            
            # 获取Steam ID
            steam_id = credentials.get("steam_id")
            if not steam_id:
                raise ToolProviderCredentialValidationError("Steam ID不能为空")
            
            # 进行API调用来验证凭证
            url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}"
            response = requests.get(url)
            
            # 验证响应状态码
            if response.status_code != 200:
                raise ToolProviderCredentialValidationError(f"API验证失败，状态码: {response.status_code}")
            
            # 检查API返回结果
            response_data = response.json()
            if 'response' not in response_data or 'players' not in response_data['response']:
                raise ToolProviderCredentialValidationError("API返回格式无效")
            
            # 验证是否找到了指定的用户
            players = response_data['response']['players']
            if not players:
                raise ToolProviderCredentialValidationError(f"未找到指定的Steam ID: {steam_id}")
                
        except ToolProviderCredentialValidationError:
            # 直接重新抛出自定义的验证错误
            raise
        except Exception as e:
            # 处理其他可能的错误
            raise ToolProviderCredentialValidationError(f"凭证验证失败: {str(e)}")
    
    def get_player_summary(self, steam_id: str) -> dict:
        """获取Steam用户的个人资料信息"""
        api_key = self.credentials.get('api_key')
        if not api_key:
            return {"success": False, "message": "API Key不存在"}
        
        try:
            url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}"
            response = requests.get(url)
            
            if response.status_code != 200:
                return {"success": False, "message": f"Steam API请求失败: HTTP状态码 {response.status_code}"}
            
            data = response.json()
            
            if 'response' not in data or 'players' not in data['response']:
                return {"success": False, "message": "API返回格式无效"}
            
            players = data['response']['players']
            if not players:
                return {"success": False, "message": f"未找到指定的Steam ID: {steam_id}"}
            
            player = players[0]
            return {
                "success": True,
                "player": {
                    "steamid": player.get('steamid'),
                    "personaname": player.get('personaname'),
                    "profileurl": player.get('profileurl'),
                    "avatar": player.get('avatar'),
                    "avatarmedium": player.get('avatarmedium'),
                    "avatarfull": player.get('avatarfull'),
                    "personastate": player.get('personastate'),
                    "lastlogoff": player.get('lastlogoff'),
                    "timecreated": player.get('timecreated'),
                    "communityvisibilitystate": player.get('communityvisibilitystate')
                }
            }
            
        except Exception as e:
            return {"success": False, "message": f"获取玩家资料失败: {str(e)}"}
