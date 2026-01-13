import requests , os , psutil , sys , jwt , pickle , json , binascii , time , urllib3 , base64 , datetime , re , socket , threading , ssl , pytz , aiohttp
from protobuf_decoder.protobuf_decoder import Parser
from xC4 import * ; from xHeaders import *
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Pb2 import DEcwHisPErMsG_pb2 , MajoRLoGinrEs_pb2 , PorTs_pb2 , MajoRLoGinrEq_pb2 , sQ_pb2 , Team_msg_pb2
from cfonts import render, say
import asyncio
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  

# VariabLes dyli 
#------------------------------------------#
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
fast_spam_running = False
fast_spam_task = None
custom_spam_running = False
custom_spam_task = None
spam_request_running = False
spam_request_task = None
evo_fast_spam_running = False
evo_fast_spam_task = None
evo_custom_spam_running = False
evo_custom_spam_task = None
lag_running = False
lag_task = None
#------------------------------------------#

# Emote mapping for evo commands
EMOTE_MAP = {
    1: 909000063,
    2: 909000068,
    3: 909000075,
    4: 909000081,
    5: 909000085,
    6: 909000098,
    7: 909000090,
    8: 909033002,
    9: 909035007,
    10: 909033001,
    11: 909037011,
    12: 909035012,
    13: 909038010,
    14: 909039011,
    15: 909040010,
    16: 909041005,
    17: 909042008,
    18: 909045001,
    19: 909038012,
    20: 909049010,
    21: 909051003
}
# Emote mapping for em commands
EMOTE_MAP_2 = {
    1:   909000001,
    2:   909000002,
    3:   909000003,
    4:   909000004,
    5:   909000005,
    6:   909000006,
    7:   909000007,
    8:   909000008,
    9:   909000009,
    10:  909000010,
    11:  909000011,
    12:  909000012,
    13:  909000013,
    14:  909000014,
    15:  909000015,
    16:  909000016,
    17:  909000017,
    18:  909000018,
    19:  909000019,
    20:  909000020,
    21:  909000021,
    22:  909000022,
    23:  909000023,
    24:  909000024,
    25:  909000025,
    26:  909000026,
    27:  909000027,
    28:  909000028,
    29:  909000029,
    30:  909000031,
    31:  909000032,
    32:  909000033,
    33:  909000034,
    34:  909000035,
    35:  909000036,
    36:  909000037,
    37:  909000038,
    38:  909000039,
    39:  909000040,
    40:  909000041,
    41:  909000042,
    42:  909000043,
    43:  909000044,
    44:  909000045,
    45:  909000046,
    46:  909000047,
    47:  909000048,
    48:  909000049,
    49:  909000051,
    50:  909000052,
    51:  909000053,
    52:  909000054,
    53:  909000055,
    54:  909000056,
    55:  909000057,
    56:  909000058,
    57:  909000059,
    58:  909000060,
    59:  909000061,
    60:  909000062,
    61:  909000063,
    62:  909000064,
    63:  909000065,
    64:  909000066,
    65:  909000067,
    66:  909000068,
    67:  909000069,
    68:  909000070,
    69:  909000071,
    70:  909000072,
    71:  909000073,
    72:  909000074,
    73:  909000075,
    74:  909000076,
    75:  909000077,
    76:  909000078,
    77:  909000079,
    78:  909000080,
    79:  909000081,
    80:  909000082,
    81:  909000083,
    82:  909000084,
    83:  909000085,
    84:  909000086,
    85:  909000087,
    86:  909000088,
    87:  909000089,
    88:  909000090,
    89:  909000091,
    90:  909000092,
    91:  909000093,
    92:  909000094,
    93:  909000095,
    94:  909000096,
    95:  909000097,
    106: 909000108,
    119: 909000121,
    120: 909000122,
    121: 909000123,
    122: 909000124,
    123: 909000125,
    124: 909000126,
    125: 909000127,
    126: 909000128,
    127: 909000129,
    128: 909000130,
    129: 909000131,
    130: 909000132,
    131: 909000133,
    132: 909000134,
    133: 909000135,
    134: 909000136,
    135: 909000137,
    136: 909000138,
    137: 909000139,
    138: 909000140,
    139: 909000141,
    140: 909000142,
    142: 909000144,
    143: 909000145,
    144: 909000150,
    145: 909033001,
    146: 909033002,
    147: 909033003,
    148: 909033004,
    149: 909033005,
    150: 909033006,
    151: 909033007,
    152: 909033008,
    153: 909033009,
    154: 909033010,
    155: 909034001,
    156: 909034002,
    157: 909034003,
    158: 909034004,
    159: 909034005,
    160: 909034006,
    161: 909034007,
    162: 909034008,
    163: 909034009,
    164: 909034010,
    165: 909034011,
    166: 909034012,
    167: 909034013,
    168: 909034014,
    169: 909035001,
    173: 909035005,
    174: 909035006,
    175: 909035007,
    176: 909035008,
    177: 909035009,
    178: 909035010,
    179: 909035011,
    180: 909035012,
    181: 909035013,
    182: 909035014,
    183: 909035015,
    184: 909036001,
    185: 909036002,
    186: 909036003,
    187: 909036004,
    188: 909036005,
    189: 909036006,
    190: 909036008,
    191: 909036009,
    192: 909036010,
    193: 909036011,
    194: 909036012,
    195: 909036014,
    196: 909037001,
    197: 909037002,
    198: 909037003,
    199: 909037004,
    200: 909037005,
    201: 909037006,
    202: 909037007,
    203: 909037008,
    204: 909037009,
    205: 909037010,
    206: 909037011,
    207: 909037012,
    208: 909038001,
    210: 909038003,
    211: 909038004,
    212: 909038005,
    213: 909038006,
    214: 909038008,
    215: 909038009,
    216: 909038010,
    217: 909038011,
    218: 909038012,
    219: 909038013,
    220: 909039001,
    221: 909039002,
    222: 909039003,
    223: 909039004,
    224: 909039005,
    225: 909039006,
    226: 909039007,
    227: 909039008,
    228: 909039009,
    229: 909039010,
    230: 909039011,
    231: 909039012,
    232: 909039013,
    233: 909039014,
    234: 909040001,
    235: 909040002,
    236: 909040003,
    237: 909040004,
    238: 909040005,
    239: 909040006,
    240: 909040008,
    241: 909040009,
    242: 909040010,
    243: 909040011,
    244: 909040012,
    245: 909040013,
    247: 909041001,
    248: 909041002,
    249: 909041003,
    250: 909041004,
    251: 909041005,
    252: 909041006,
    253: 909041007,
    254: 909041008,
    255: 909041009,
    256: 909041010,
    257: 909041011,
    258: 909041012,
    259: 909041013,
    260: 909041014,
    261: 909041015,
    262: 909042001,
    263: 909042002,
    264: 909042003,
    265: 909042004,
    266: 909042005,
    267: 909042006,
    268: 909042007,
    269: 909042008,
    270: 909042009,
    271: 909042011,
    272: 909042012,
    274: 909042016,
    275: 909042017,
    276: 909042018,
    277: 909043001,
    278: 909043002,
    279: 909043003,
    280: 909043004,
    281: 909043005,
    282: 909043006,
    283: 909043007,
    284: 909043008,
    285: 909043009,
    288: 909044001,
    289: 909044002,
    290: 909044003,
    291: 909044004,
    292: 909044005,
    294: 909044007,
    295: 909044008,
    296: 909044009,
    297: 909044010,
    298: 909044011,
    299: 909044012,
    300: 909044015,
    301: 909044016,
    302: 909045001,
    303: 909045002,
    304: 909045003,
    305: 909045004,
    306: 909045005,
    307: 909045006,
    308: 909045007,
    309: 909045008,
    310: 909045009,
    311: 909045010,
    312: 909045011,
    314: 909045015,
    315: 909045016,
    316: 909045017,
    317: 909046001,
    318: 909046002,
    319: 909046003,
    322: 909046006,
    323: 909046007,
    324: 909046008,
    325: 909046009,
    326: 909046010,
    327: 909046011,
    328: 909046012,
    329: 909046013,
    330: 909046014,
    331: 909046015,
    332: 909046016,
    333: 909046017,
    334: 909047001,
    337: 909047004,
    338: 909047005,
    339: 909047006,
    340: 909047007,
    341: 909047008,
    342: 909047009,
    343: 909047010,
    344: 909047011,
    345: 909047012,
    346: 909047013,
    347: 909047015,
    348: 909047016,
    349: 909047017,
    350: 909047018,
    351: 909047019,
    353: 909048002,
    354: 909048003,
    355: 909048004,
    356: 909048005,
    357: 909048006,
    358: 909048007,
    359: 909048008,
    361: 909048010,
    362: 909048011,
    363: 909048012,
    364: 909048013,
    365: 909048014,
    366: 909048015,
    367: 909048016,
    368: 909048017,
    369: 909048018,
    370: 909049001,
    371: 909049002,
    372: 909049003,
    373: 909049004,
    374: 909049005,
    375: 909049006,
    376: 909049007,
    378: 909049009,
    379: 909049010,
    380: 909049011,
    381: 909049012,
    382: 909049013,
    383: 909049014,
    384: 909049015,
    385: 909049016,
    386: 909049017,
    387: 909049018,
    388: 909049019,
    389: 909049020,
    390: 909049021,
    391: 909050002,
    392: 909050003,
    393: 909050004,
    394: 909050005,
    395: 909050006,
    396: 909050008,
    397: 909050009,
    398: 909050010,
    399: 909050011,
    400: 909050012,
    401: 909050013,
    402: 909050014,
    403: 909050015,
    404: 909050016,
    405: 909050017,
    406: 909050018,
    407: 909050019,
    408: 909050020,
    409: 909050021,
    410: 909046004,
    411: 909046005,
    412: 909047002,
    413: 909047003,
    414: 909048001,
    415: 909048009,
    416: 909049008,
    417: 909050003
}
# Helper functions for ghost join
def dec_to_hex(decimal):
    """Convert decimal to hex string"""
    hex_str = hex(decimal)[2:]
    return hex_str.upper() if len(hex_str) % 2 == 0 else '0' + hex_str.upper()

async def encrypt_packet(packet_hex, key, iv):
    """Encrypt packet using AES CBC"""
    cipher = AES.new(key, AES.MODE_CBC, iv)
    packet_bytes = bytes.fromhex(packet_hex)
    padded_packet = pad(packet_bytes, AES.block_size)
    encrypted = cipher.encrypt(padded_packet)
    return encrypted.hex()

async def nmnmmmmn(packet_hex, key, iv):
    """Wrapper for encrypt_packet"""
    return await encrypt_packet(packet_hex, key, iv)

async def ghost_join_packet(player_id, secret_code, key, iv):
    """Create ghost join packet"""
    try:
        # Create a simple packet structure for joining
        # This is a basic implementation - adjust based on your needs
        packet_data = f"01{dec_to_hex(len(secret_code))}{secret_code.encode().hex()}"
        
        # Encrypt the packet
        encrypted_packet = await encrypt_packet(packet_data, key, iv)
        
        # Create header
        header_length = len(encrypted_packet) // 2
        header_length_hex = dec_to_hex(header_length)
        
        # Build final packet based on header length
        if len(header_length_hex) == 2:
            final_packet = "0515000000" + header_length_hex + encrypted_packet
        elif len(header_length_hex) == 3:
            final_packet = "051500000" + header_length_hex + encrypted_packet
        elif len(header_length_hex) == 4:
            final_packet = "05150000" + header_length_hex + encrypted_packet
        elif len(header_length_hex) == 5:
            final_packet = "0515000" + header_length_hex + encrypted_packet
        else:
            final_packet = "0515000000" + header_length_hex + encrypted_packet
            
        return bytes.fromhex(final_packet)
        
    except Exception as e:
        print(f"Error creating ghost join packet: {e}")
        return None

async def lag_team_loop(team_code, key, iv, region):
    """Rapid join/leave loop to create lag"""
    global lag_running
    count = 0
    
    while lag_running:
        try:
            # Join the team
            join_packet = await GenJoinSquadsPacket(team_code, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_packet)
            
            # Very short delay before leaving
            await asyncio.sleep(0.001)  # 10 milliseconds
            
            # Leave the team
            leave_packet = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_packet)
            
            count += 1
            print(f"Lag cycle #{count} completed for team: {team_code}")
            
            # Short delay before next cycle
            await asyncio.sleep(0.001)  # 10 milliseconds between cycles
            
        except Exception as e:
            print(f"Error in lag loop: {e}")
            # Continue the loop even if there's an error
            await asyncio.sleep(0.01)
 
####################################

#Clan-info-by-clan-id
def Get_clan_info(clan_id):
    try:
        url = f"https://get-clan-info.vercel.app/get_clan_info?clan_id={clan_id}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            msg = f""" 
[11EAFD][b][c]
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
▶▶▶▶GUILD DETAILS◀◀◀◀
Achievements: {data['achievements']}\n\n
Balance : {fix_num(data['balance'])}\n\n
Clan Name : {data['clan_name']}\n\n
Expire Time : {fix_num(data['guild_details']['expire_time'])}\n\n
Members Online : {fix_num(data['guild_details']['members_online'])}\n\n
Regional : {data['guild_details']['regional']}\n\n
Reward Time : {fix_num(data['guild_details']['reward_time'])}\n\n
Total Members : {fix_num(data['guild_details']['total_members'])}\n\n
ID : {fix_num(data['id'])}\n\n
Last Active : {fix_num(data['last_active'])}\n\n
Level : {fix_num(data['level'])}\n\n
Rank : {fix_num(data['rank'])}\n\n
Region : {data['region']}\n\n
Score : {fix_num(data['score'])}\n\n
Timestamp1 : {fix_num(data['timestamp1'])}\n\n
Timestamp2 : {fix_num(data['timestamp2'])}\n\n
Welcome Message: {data['welcome_message']}\n\n
XP: {fix_num(data['xp'])}\n\n
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
[FFB300][b][c]MADE BY THE Meowl CODEX
            """
            return msg
        else:
            msg = """
[11EAFD][b][c]
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
Failed to get info, please try again later!!

°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
[FFB300][b][c]MADE BY THE Meowl CODEX
            """
            return msg
    except:
        pass
#GET INFO BY PLAYER ID
def get_player_info(player_id):
    url = f"https://like2.vercel.app/player-info?uid={player_id}&server={2}&key={2}"
    response = requests.get(url)
    print(response)    
    if response.status_code == 200:
        try:
            r = response.json()
            return {
                "Account Booyah Pass": f"{r.get('booyah_pass_level', 'N/A')}",
                "Account Create": f"{r.get('createAt', 'N/A')}",
                "Account Level": f"{r.get('level', 'N/A')}",
                "Account Likes": f" {r.get('likes', 'N/A')}",
                "Name": f"{r.get('nickname', 'N/A')}",
                "UID": f" {r.get('accountId', 'N/A')}",
                "Account Region": f"{r.get('region', 'N/A')}",
                }
        except ValueError as e:
            pass
            return {
                "error": "Invalid JSON response"
            }
    else:
        pass
        return {
            "error": f"Failed to fetch data: {response.status_code}"
        }
#CHAT WITH AI
def talk_with_ai(question):
    url = f"https://gemini-api-api-v2.vercel.app/prince/api/v1/ask?key=prince&ask={question}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        msg = data["message"]["content"]
        return msg
    else:
        return "An error occurred while connecting to the server."
#SPAM REQUESTS
def spam_requests(player_id):
    # This URL now correctly points to the Flask app you provided
    url = f"https://like2.vercel.app/send_requests?uid={player_id}&server={2}&key={2}"
    try:
        res = requests.get(url, timeout=20) # Added a timeout
        if res.status_code == 200:
            data = res.json()
            # Return a more descriptive message based on the API's JSON response
            return f"API Status: Success [{data.get('success_count', 0)}] Failed [{data.get('failed_count', 0)}]"
        else:
            # Return the error status from the API
            return f"API Error: Status {res.status_code}"
    except requests.exceptions.RequestException as e:
        # Handle cases where the API isn't running or is unreachable
        print(f"Could not connect to spam API: {e}")
        return "Failed to connect to spam API."
####################################

# ** NEW INFO FUNCTION using the new API **
def newinfo(uid):
    # Base URL without parameters
    url = "https://like2.vercel.app/player-info"
    # Parameters dictionary - this is the robust way to do it
    params = {
        'uid': uid,
        'server': 2,  # Hardcoded to bd as requested
        'key': 2
    }
    try:
        # Pass the parameters to requests.get()
        response = requests.get(url, params=params, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Check if the expected data structure is in the response
            if "basicInfo" in data:
                return {"status": "ok", "data": data}
            else:
                # The API returned 200, but the data is not what we expect (e.g., error message in JSON)
                return {"status": "error", "message": data.get("error", "Invalid ID or data not found.")}
        else:
            # The API returned an error status code (e.g., 404, 500)
            try:
                # Try to get a specific error message from the API's response
                error_msg = response.json().get('error', f"API returned status {response.status_code}")
                return {"status": "error", "message": error_msg}
            except ValueError:
                # If the error response is not JSON
                return {"status": "error", "message": f"API returned status {response.status_code}"}

    except requests.exceptions.RequestException as e:
        # Handle network errors (e.g., timeout, no connection)
        return {"status": "error", "message": f"Network error: {str(e)}"}
    except ValueError: 
        # Handle cases where the response is not valid JSON
        return {"status": "error", "message": "Invalid JSON response from API."}

	
#ADDING-100-LIKES-IN-24H
def send_likes(uid):
    try:
        likes_api_response = requests.get(
             f"https://yourlikeapi/like?uid={uid}&server_name={2}&x-vercel-set-bypass-cookie=true&x-vercel-protection-bypass={BYPASS_TOKEN}",
             timeout=15
             )
      
      
        if likes_api_response.status_code != 200:
            return f"""
[C][B][FF0000]━━━━━
[FFFFFF]Like API Error!
Status Code: {likes_api_response.status_code}
Please check if the uid is correct.
━━━━━
"""

        api_json_response = likes_api_response.json()

        player_name = api_json_response.get('PlayerNickname', 'Unknown')
        likes_before = api_json_response.get('LikesbeforeCommand', 0)
        likes_after = api_json_response.get('LikesafterCommand', 0)
        likes_added = api_json_response.get('LikesGivenByAPI', 0)
        status = api_json_response.get('status', 0)

        if status == 1 and likes_added > 0:
            # ✅ Success
            return f"""
[C][B][11EAFD]‎━━━━━━━━━━━━
[FFFFFF]Likes Status:

[FFD3EF]Likes Sent Successfully!

[FFFFFF]Player Name : [FFD3EF]{player_name}  
[FFFFFF]Likes Added : [FFD3EF]{likes_added}  
[FFFFFF]Likes Before : [FFD3EF]{likes_before}  
[FFFFFF]Likes After : [FFD3EF]{likes_after}  
[C][B][11EAFD]‎━━━━━━━━━━━━
[C][B][FFB300]Subscribe: [FFFFFF]SPIDEERIO YT [FFD3EF]!!
"""
        elif status == 2 or likes_before == likes_after:
            # 🚫 Already claimed / Maxed
            return f"""
[C][B][FF0000]━━━━━━━━━━━━

[FFFFFF]No Likes Sent!

[FF0000]You have already taken likes with this UID.
Try again after 24 hours.

[FFFFFF]Player Name : [FF0000]{player_name}  
[FFFFFF]Likes Before : [FF0000]{likes_before}  
[FFFFFF]Likes After : [FF0000]{likes_after}  
[C][B][FF0000]━━━━━━━━━━━━
"""
        else:
            # ❓ Unexpected case
            return f"""
[C][B][FF0000]━━━━━━━━━━━━
[FFFFFF]Unexpected Response!
Something went wrong.

Please try again or contact support.
━━━━━━━━━━━━
"""

    except requests.exceptions.RequestException:
        return """
[C][B][FF0000]━━━━━
[FFFFFF]Like API Connection Failed!
Is the API server (app.py) running?
━━━━━
"""
    except Exception as e:
        return f"""
[C][B][FF0000]━━━━━
[FFFFFF]An unexpected error occurred:
[FF0000]{str(e)}
━━━━━
"""
####################################
#CHECK ACCOUNT IS BANNED

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB51"}

# ---- Random Colores ----
def get_random_color():
    colors = [
        "[FF0000]", "[FFD3EF]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[FFD3EF]", "[FFFFFF]", "[FFA500]",
        "[A52A2A]", "[800080]", "[000000]", "[808080]", "[C0C0C0]", "[FFC0CB]", "[FFD700]", "[ADD8E6]",
        "[90EE90]", "[D2691E]", "[DC143C]", "[00CED1]", "[9400D3]", "[F08080]", "[20B2AA]", "[FF1493]",
        "[7CFC00]", "[B22222]", "[FF4500]", "[DAA520]", "[00BFFF]", "[00FF7F]", "[4682B4]", "[6495ED]",
        "[5F9EA0]", "[DDA0DD]", "[E6E6FA]", "[B0C4DE]", "[556B2F]", "[8FBC8F]", "[2E8B57]", "[3CB371]",
        "[6B8E23]", "[808000]", "[B8860B]", "[CD5C5C]", "[8B0000]", "[FF6347]", "[FF8C00]", "[BDB76B]",
        "[9932CC]", "[8A2BE2]", "[4B0082]", "[6A5ACD]", "[7B68EE]", "[4169E1]", "[1E90FF]", "[191970]",
        "[00008B]", "[000080]", "[008080]", "[008B8B]", "[B0E0E6]", "[AFEEEE]", "[E0FFFF]", "[F5F5DC]",
        "[FAEBD7]"
    ]
    return random.choice(colors)

async def encrypted_proto(encoded_hex):
    key = b'Yg&tc%DEuh6%Zc^8'
    iv = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(encoded_hex, AES.block_size)
    encrypted_payload = cipher.encrypt(padded_message)
    return encrypted_payload
    
async def GeNeRaTeAccEss(uid , password):
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    headers = {
        "Host": "100067.connect.garena.com",
        "User-Agent": (await Ua()),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "close"}
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200: return "Failed to get access token"
            data = await response.json()
            open_id = data.get("open_id")
            access_token = data.get("access_token")
            return (open_id, access_token) if open_id and access_token else (None, None)
async def EncRypTMajoRLoGin(open_id, access_token):
    major_login = MajoRLoGinrEq_pb2.MajorLogin()
    major_login.event_time = str(datetime.now())[:-7]
    major_login.game_name = "free fire"
    major_login.platform_id = 1
    major_login.client_version = "1.118.1"
    major_login.system_software = "Android OS 9 / API-28 (PQ3B.190801.10101846/G9650ZHU2ARC6)"
    major_login.system_hardware = "Handheld"
    major_login.telecom_operator = "Verizon"
    major_login.network_type = "WIFI"
    major_login.screen_width = 1920
    major_login.screen_height = 1080
    major_login.screen_dpi = "280"
    major_login.processor_details = "ARM64 FP ASIMD AES VMH | 2865 | 4"
    major_login.memory = 3003
    major_login.gpu_renderer = "Adreno (TM) 640"
    major_login.gpu_version = "OpenGL ES 3.1 v1.46"
    major_login.unique_device_id = "Google|34a7dcdf-a7d5-4cb6-8d7e-3b0e448a0c57"
    major_login.client_ip = "223.191.51.89"
    major_login.language = "en"
    major_login.open_id = open_id
    major_login.open_id_type = "4"
    major_login.device_type = "Handheld"
    memory_available = major_login.memory_available
    memory_available.version = 55
    memory_available.hidden_value = 81
    major_login.access_token = access_token
    major_login.platform_sdk_id = 1
    major_login.network_operator_a = "Verizon"
    major_login.network_type_a = "WIFI"
    major_login.client_using_version = "7428b253defc164018c604a1ebbfebdf"
    major_login.external_storage_total = 36235
    major_login.external_storage_available = 31335
    major_login.internal_storage_total = 2519
    major_login.internal_storage_available = 703
    major_login.game_disk_storage_available = 25010
    major_login.game_disk_storage_total = 26628
    major_login.external_sdcard_avail_storage = 32992
    major_login.external_sdcard_total_storage = 36235
    major_login.login_by = 3
    major_login.library_path = "/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/lib/arm64"
    major_login.reg_avatar = 1
    major_login.library_token = "5b892aaabd688e571f688053118a162b|/data/app/com.dts.freefireth-YPKM8jHEwAJlhpmhDhv5MQ==/base.apk"
    major_login.channel_type = 3
    major_login.cpu_type = 2
    major_login.cpu_architecture = "64"
    major_login.client_version_code = "2019118695"
    major_login.graphics_api = "OpenGLES2"
    major_login.supported_astc_bitset = 16383
    major_login.login_open_id_type = 4
    major_login.analytics_detail = b"FwQVTgUPX1UaUllDDwcWCRBpWA0FUgsvA1snWlBaO1kFYg=="
    major_login.loading_time = 13564
    major_login.release_channel = "android"
    major_login.extra_info = "KqsHTymw5/5GB23YGniUYN2/q47GATrq7eFeRatf0NkwLKEMQ0PK5BKEk72dPflAxUlEBir6Vtey83XqF593qsl8hwY="
    major_login.android_engine_init_flag = 110009
    major_login.if_push = 1
    major_login.is_vpn = 1
    major_login.origin_platform_type = "4"
    major_login.primary_platform_type = "4"
    string = major_login.SerializeToString()
    return  await encrypted_proto(string)

async def MajorLogin(payload):
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def GetLoginData(base_url, payload, token):
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization']= f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200: return await response.read()
            return None

async def DecRypTMajoRLoGin(MajoRLoGinResPonsE):
    proto = MajoRLoGinrEs_pb2.MajorLoginRes()
    proto.ParseFromString(MajoRLoGinResPonsE)
    return proto

async def DecRypTLoGinDaTa(LoGinDaTa):
    proto = PorTs_pb2.GetLoginData()
    proto.ParseFromString(LoGinDaTa)
    return proto

async def DecodeWhisperMessage(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = DEcwHisPErMsG_pb2.DecodeWhisper()
    proto.ParseFromString(packet)
    return proto
    
async def decode_team_packet(hex_packet):
    packet = bytes.fromhex(hex_packet)
    proto = sQ_pb2.recieved_chat()
    proto.ParseFromString(packet)
    return proto
    
async def xAuThSTarTuP(TarGeT, token, timestamp, key, iv):
    uid_hex = hex(TarGeT)[2:]
    uid_length = len(uid_hex)
    encrypted_timestamp = await DecodE_HeX(timestamp)
    encrypted_account_token = token.encode().hex()
    encrypted_packet = await EnC_PacKeT(encrypted_account_token, key, iv)
    encrypted_packet_length = hex(len(encrypted_packet) // 2)[2:]
    if uid_length == 9: headers = '0000000'
    elif uid_length == 8: headers = '00000000'
    elif uid_length == 10: headers = '000000'
    elif uid_length == 7: headers = '000000000'
    else: print('Unexpected length') ; headers = '0000000'
    return f"0115{headers}{uid_hex}{encrypted_timestamp}00000{encrypted_packet_length}{encrypted_packet}"
async def cHTypE(H):
    if not H: return 'Squid'
    elif H == 1: return 'CLan'
    elif H == 2: return 'PrivaTe'
    
async def SEndMsG(H , message , Uid , chat_id , key , iv):
    TypE = await cHTypE(H)
    if TypE == 'Squid': msg_packet = await xSEndMsgsQ(message , chat_id , key , iv)
    elif TypE == 'CLan': msg_packet = await xSEndMsg(message , 1 , chat_id , chat_id , key , iv)
    elif TypE == 'PrivaTe': msg_packet = await xSEndMsg(message , 2 , Uid , Uid , key , iv)
    return msg_packet

async def SEndPacKeT(OnLinE , ChaT , TypE , PacKeT):
    if TypE == 'ChaT' and ChaT: whisper_writer.write(PacKeT) ; await whisper_writer.drain()
    elif TypE == 'OnLine': online_writer.write(PacKeT) ; await online_writer.drain()
    else: return 'UnsoPorTed TypE ! >> ErrrroR (:():)' 

async def safe_send_message(chat_type, message, target_uid, chat_id, key, iv, max_retries=3):
    """Safely send message with retry mechanism"""
    for attempt in range(max_retries):
        try:
            P = await SEndMsG(chat_type, message, target_uid, chat_id, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'ChaT', P)
            print(f"Message sent successfully on attempt {attempt + 1}")
            return True
        except Exception as e:
            print(f"Failed to send message (attempt {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(0.5)  # Wait before retry
    return False

async def fast_emote_spam(uids, emote_id, key, iv, region):
    """Fast emote spam function that sends emotes rapidly"""
    global fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    while fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, int(emote_id), key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # 0.1 seconds interval between spam cycles
async def send_menu(chat_type, content, uid, chat_id, key, iv):
    await safe_send_message(chat_type, content, uid, chat_id, key, iv)
    await asyncio.sleep(0.6)
# NEW FUNCTION: Custom emote spam with specified times
async def custom_emote_spam(uid, emote_id, times, key, iv, region):
    """Custom emote spam function that sends emotes specified number of times"""
    global custom_spam_running
    count = 0
    
    while custom_spam_running and count < times:
        try:
            uid_int = int(uid)
            H = await Emote_k(uid_int, int(emote_id), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            count += 1
            await asyncio.sleep(0.1)  # 0.1 seconds interval between emotes
        except Exception as e:
            print(f"Error in custom_emote_spam for uid {uid}: {e}")
            break

# NEW FUNCTION: Faster spam request loop - Sends exactly 30 requests quickly
async def spam_request_loop(target_uid, key, iv, region):
    """Spam request function that creates group and sends join requests in loop - FASTER VERSION"""
    global spam_request_running
    count = 0
    max_requests = 1000  # Send exactly 30 requests
    
    while spam_request_running and count < max_requests:
        try:
            # Create squad
            PAc = await OpEnSq(key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
            await asyncio.sleep(0.01)  # Reduced delay
            
            # Send invite
            V = await SEnd_InV(5, int(target_uid), key, iv, region)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
            
            # Leave squad immediately without waiting
            E = await ExiT(None, key, iv)
            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
            
            count += 1
            print(f"Sent request #{count} to {target_uid}")
            
            # Shorter delay between requests
            await asyncio.sleep(0.1)  # Reduced from 1 second to 0.5 seconds
            
        except Exception as e:
            print(f"Error in spam_request_loop for uid {target_uid}: {e}")
            # Continue with next request instead of breaking
            await asyncio.sleep(0.1)
# NEW FUNCTION: Evolution emote spam with mapping
async def evo_emote_spam(uids, number, key, iv, region):
    """Send evolution emotes based on number mapping"""
    try:
        emote_id = EMOTE_MAP.get(int(number))
        if not emote_id:
            return False, f"Invalid number! Use 1-21 only."
        
        success_count = 0
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                success_count += 1
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Error sending evo emote to {uid}: {e}")
        
        return True, f"Sent evolution emote {number} (ID: {emote_id}) to {success_count} player(s)"
    
    except Exception as e:
        return False, f"Error in evo_emote_spam: {str(e)}"

# NEW FUNCTION: Fast evolution emote spam
async def evo_fast_emote_spam(uids, number, key, iv, region):
    """Fast evolution emote spam function"""
    global evo_fast_spam_running
    count = 0
    max_count = 25  # Spam 25 times
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_fast_spam_running and count < max_count:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in evo_fast_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed fast evolution emote spam {count} times"

# NEW FUNCTION: Custom evolution emote spam with specified times
async def evo_custom_emote_spam(uids, number, times, key, iv, region):
    """Custom evolution emote spam with specified repeat times"""
    global evo_custom_spam_running
    count = 0
    
    emote_id = EMOTE_MAP.get(int(number))
    if not emote_id:
        return False, f"Invalid number! Use 1-21 only."
    
    while evo_custom_spam_running and count < times:
        for uid in uids:
            try:
                uid_int = int(uid)
                H = await Emote_k(uid_int, emote_id, key, iv, region)
                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
            except Exception as e:
                print(f"Error in evo_custom_emote_spam for uid {uid}: {e}")
        
        count += 1
        await asyncio.sleep(0.1)  # CHANGED: 0.5 seconds to 0.1 seconds
    
    return True, f"Completed custom evolution emote spam {count} times"

async def TcPOnLine(ip, port, key, iv, AutHToKen, reconnect_delay=0.5):
    global online_writer , spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , XX , uid , Spy,data2, Chat_Leave, fast_spam_running, fast_spam_task, custom_spam_running, custom_spam_task, spam_request_running, spam_request_task, evo_fast_spam_running, evo_fast_spam_task, evo_custom_spam_running, evo_custom_spam_task, lag_running, lag_task
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            online_writer.write(bytes_payload)
            await online_writer.drain()
            while True:
                data2 = await reader.read(9999)
                if not data2: break
                
                if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                    try:
                        print(data2.hex()[10:])
                        packet = await DeCode_PackEt(data2.hex()[10:])
                        print(packet)
                        packet = json.loads(packet)
                        OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                        JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)


                        message = f'[B][C]{get_random_color()}\nXin chào tôi là iw.Nguyen Tieu ! \n\n{get_random_color()} Nhập lệnh : /help để xem các tùy chọn'
                        P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                        await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)

                    except:
                        if data2.hex().startswith('0500') and len(data2.hex()) > 1000:
                            try:
                                print(data2.hex()[10:])
                                packet = await DeCode_PackEt(data2.hex()[10:])
                                print(packet)
                                packet = json.loads(packet)
                                OwNer_UiD , CHaT_CoDe , SQuAD_CoDe = await GeTSQDaTa(packet)

                                JoinCHaT = await AutH_Chat(3 , OwNer_UiD , CHaT_CoDe, key,iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , JoinCHaT)


                                message = f'[B][C]{get_random_color()}\nXin chào tôi là iw.Nguyen Tieu ! \n\n{get_random_color()} Nhập lệnh : /help để xem các tùy chọn'
                                P = await SEndMsG(0 , message , OwNer_UiD , OwNer_UiD , key , iv)
                                await SEndPacKeT(whisper_writer , online_writer , 'ChaT' , P)
                            except:
                                pass

            online_writer.close() ; await online_writer.wait_closed() ; online_writer = None

        except Exception as e: print(f"- ErroR With {ip}:{port} - {e}") ; online_writer = None
        await asyncio.sleep(reconnect_delay)
                            
async def TcPChaT(ip, port, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region , reconnect_delay=0.5):
    print(region, 'TCP CHAT')

    global spam_room , whisper_writer , spammer_uid , spam_chat_id , spam_uid , online_writer , chat_id , XX , uid , Spy,data2, Chat_Leave, fast_spam_running, fast_spam_task, custom_spam_running, custom_spam_task, spam_request_running, spam_request_task, evo_fast_spam_running, evo_fast_spam_task, evo_custom_spam_running, evo_custom_spam_task, lag_running, lag_task
    while True:
        try:
            reader , writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            bytes_payload = bytes.fromhex(AutHToKen)
            whisper_writer.write(bytes_payload)
            await whisper_writer.drain()
            ready_event.set()
            if LoGinDaTaUncRypTinG.Clan_ID:
                clan_id = LoGinDaTaUncRypTinG.Clan_ID
                clan_compiled_data = LoGinDaTaUncRypTinG.Clan_Compiled_Data
                print('\n - TarGeT BoT in CLan ! ')
                print(f' - Clan Uid > {clan_id}')
                print(f' - BoT ConnEcTed WiTh CLan ChaT SuccEssFuLy ! ')
                pK = await AuthClan(clan_id , clan_compiled_data , key , iv)
                if whisper_writer: whisper_writer.write(pK) ; await whisper_writer.drain()
            while True:
                data = await reader.read(9999)
                if not data: break
                
                if data.hex().startswith("120000"):

                    msg = await DeCode_PackEt(data.hex()[10:])
                    chatdata = json.loads(msg)
                    try:
                        response = await DecodeWhisperMessage(data.hex()[10:])
                        uid = response.Data.uid
                        chat_id = response.Data.Chat_ID
                        XX = response.Data.chat_type
                        inPuTMsG = response.Data.msg.lower()
                        
                        # Debug print to see what we're receiving
                        print(f"Received message: {inPuTMsG} from UID: {uid} in chat type: {XX}")
                        
                    except:
                        response = None


                    if response:
                        # ALL COMMANDS NOW WORK IN ALL CHAT TYPES (SQUAD, GUILD, PRIVATE)
                        
                        # AI Command - /ai
                        if inPuTMsG.strip().startswith('/ai '):
                            print('Processing AI command in any chat type')
                            
                            question = inPuTMsG[4:].strip()
                            if question:
                                initial_message = f"[B][C]{get_random_color()}\n🤖 AI is thinking...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    ai_response = await loop.run_in_executor(executor, talk_with_ai, question)
                                
                                # Format the AI response
                                ai_message = f"""
[B][C][FFD3EF]🤖 AI Response:

[FFFFFF]{ai_response}

[C][B][FFB300]Question: [FFFFFF]{question}
"""
                                await safe_send_message(response.Data.chat_type, ai_message, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Please provide a question after /ai\nExample: /ai What is Free Fire?\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Likes Command - /likes
                        if inPuTMsG.strip().startswith('/likes '):
                            print('Processing likes command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /likes (uid)\nExample: /likes 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nSending 100 likes to {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                # Use ThreadPoolExecutor to avoid blocking the async loop
                                loop = asyncio.get_event_loop()
                                with ThreadPoolExecutor() as executor:
                                    likes_result = await loop.run_in_executor(executor, send_likes, target_uid)
                                
                                await safe_send_message(response.Data.chat_type, likes_result, uid, chat_id, key, iv)

                        # Invite Command - /inv (creates 5-player group and sends request)
                        if inPuTMsG.strip().startswith('/inv '):
                            print('Processing invite command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /inv (uid)\nExample: /inv 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                target_uid = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nCreating 5-Player Group and sending request to {target_uid}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Fast squad creation and invite for 5 players
                                    PAc = await OpEnSq(key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                                    await asyncio.sleep(0.3)
                                    
                                    C = await cHSq(5, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                                    await asyncio.sleep(0.3)
                                    
                                    V = await SEnd_InV(5, int(target_uid), key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                                    await asyncio.sleep(0.3)
                                    
                                    E = await ExiT(None, key, iv)
                                    await asyncio.sleep(2)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                                    
                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][FFD3EF]✅ SUCCESS! 5-Player Group invitation sent successfully to {target_uid}!\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR sending invite: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/6")):
                            # Process /6 command - Create 4 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 6-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 4 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(6, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFD3EF]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/3")):
                            # Process /3 command - Create 3 player group
                            initial_message = f"[B][C]{get_random_color()}\n\nCreating 3-Player Group...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite for 6 players
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(3, uid, key, iv, region)
                            await asyncio.sleep(0.3)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFD3EF]✅ SUCCESS! 6-Player Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.startswith(("/5")):
                            # Process /5 command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\n\nSending Group Invitation...\n\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            # Fast squad creation and invite
                            PAc = await OpEnSq(key, iv, region)
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', PAc)
                            
                            C = await cHSq(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', C)
                            
                            V = await SEnd_InV(5, uid, key, iv, region)
                            await asyncio.sleep(0.3)  # Reduced delay
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                            
                            E = await ExiT(None, key, iv)
                            await asyncio.sleep(3.5)  # Reduced from 3 seconds
                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', E)
                            await asyncio.sleep(0.2)
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFD3EF]✅ SUCCESS! Group invitation sent successfully to {uid}!\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.strip() == "/dev":
                            # Process /admin command in any chat type
                            dev_message = """
[C][B][FF0000]╔══════════╗
[FFFFFF]✨ Admin
[FFFFFF] ⚡Nguyễn Tiêu
[FFFFFF] Cảm ơn vì đã ủng hộ tôi
[FF0000]╠══════════╣
[FFD700]⚡ Chủ sở hữu : [FFFFFF]Nguyễn Tiêu 
[FFD700]✨ TikTok : [FFFFFF]@nguyentieulive
[FF0000]╚══════════╝
[FFD700]✨ Developer —͟͞͞ </> Nguyễn Tiêu ⚡
"""
                            await safe_send_message(response.Data.chat_type, dev_message, uid, chat_id, key, iv)

                        if inPuTMsG.startswith('/join'):
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /join (team_code)\nExample: /join ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nJoining squad with code: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                        
                                try:
                                    # Thử join bình thường
                                    EM = await GenJoinSquadsPacket(CodE, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
                        
                                    # SUCCESS MESSAGE
                                    success_message = f"[B][C][FFD3EF]✅ SUCCESS! Joined squad with code: {CodE}!\n"
                                    await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                        
                                    # --- Sau khi join, đợi 0.4s rồi gửi emote 909043002 ---
                                    await asyncio.sleep(0.5)
                                    emote_id = 909050009
                                    target_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                                    H = await Emote_k(target_uid, emote_id, key, iv, region)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                    emote_message = f"[B][C][FFD3EF]✅ Emote {emote_id} sent after joining squad!\n"
                                    await safe_send_message(response.Data.chat_type, emote_message, uid, chat_id, key, iv)
                        
                                except Exception as e:
                                    print(f"Regular join failed, trying ghost join: {e}")
                                    # Nếu join bình thường thất bại, thử ghost join
                                    try:
                                        bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                                        ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                        if ghost_packet:
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                                            success_message = f"[B][C][FFD3EF]✅ SUCCESS! Ghost joined squad with code: {CodE}!\n"
                                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                        
                                            # --- Ghost join thành công, gửi emote luôn ---
                                            await asyncio.sleep(0.4)
                                            emote_id = 909043002
                                            H = await Emote_k(bot_uid, emote_id, key, iv, region)
                                            await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                            emote_message = f"[B][C][FFD3EF]✅ Emote {emote_id} sent after ghost joining!\n"
                                            await safe_send_message(response.Data.chat_type, emote_message, uid, chat_id, key, iv)
                                        else:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Failed to create ghost join packet.\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        
                                    except Exception as ghost_error:
                                        print(f"Ghost join also failed: {ghost_error}")
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Failed to join squad: {str(ghost_error)}\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)          
                        # NEW GHOST COMMAND
                        if inPuTMsG.strip().startswith('/ghost'):
                            # Process /ghost command in any chat type
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /ghost (team_code)\nExample: /ghost ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                CodE = parts[1]
                                initial_message = f"[B][C]{get_random_color()}\nGhost joining squad with code: {CodE}...\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                                
                                try:
                                    # Get bot's UID from global context or login data
                                    bot_uid = LoGinDaTaUncRypTinG.AccountUID if hasattr(LoGinDaTaUncRypTinG, 'AccountUID') else TarGeT
                                    
                                    ghost_packet = await ghost_join_packet(bot_uid, CodE, key, iv)
                                    if ghost_packet:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', ghost_packet)
                                        success_message = f"[B][C][FFD3EF]✅ SUCCESS! Ghost joined squad with code: {CodE}!\n"
                                        await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                                    else:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Failed to create ghost join packet.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Ghost join failed: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        # NEW LAG COMMAND
                        if inPuTMsG.strip().startswith('/lag '):
                            print('Processing lag command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /lag (team_code)\nExample: /lag ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                                
                                # Stop any existing lag task
                                if lag_task and not lag_task.done():
                                    lag_running = False
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)
                                
                                # Start new lag task
                                lag_running = True
                                lag_task = asyncio.create_task(lag_team_loop(team_code, key, iv, region))
                                
                                # SUCCESS MESSAGE
                                success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Lag attack started!\nTeam: {team_code}\nAction: Rapid join/leave\nSpeed: Ultra fast (0.001 milisecond)\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                        # STOP LAG COMMAND
                        if inPuTMsG.strip() == '/stop lag':
                            lag_running = False
                            if lag_task and not lag_task.done():
                                lag_task.cancel()
                                try:
                                    await lag_task
                                except:
                                    pass
                                success_msg = f"[B][C][FFD3EF]🛑 SUCCESS! Lag attack stopped successfully!\n"
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active lag attack to stop!\n"
                            
                            await safe_send_message(response.Data.chat_type, success_msg if lag_running == False else error_msg, uid, chat_id, key, iv)
                        if inPuTMsG.startswith('/exit'):
                            # Process /exit command in any chat type
                            initial_message = f"[B][C]{get_random_color()}\nĐang thoát đội...\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            leave = await ExiT(uid,key,iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , leave)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[B][C][FFD3EF]✅ Thoát đội thành công\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)

                        if inPuTMsG.strip().startswith('/id'):
                            # Process /s command in any chat type
                            initial_message = f"[C][B][FFD700]═══⚓︎ EMOTE IDS MENU 1/2 ⚓︎═══[FFD3EF]\n[B][FFFFFF]⚡ 909050002 (ninja)\n[FFFFFF]⚡ 909042007 (100 lvl)\n[FFFFFF]⚡ 909050028 (auraboat)\n[FFFFFF]⚡ 909049012 (flying guns)\n[FFFFFF]⚡ 909000045 (I heart you)\n[FFFFFF]⚡ 909000034 (pirate flag)\n[FFFFFF]⚡ 909000012 (push up)\n[FFFFFF]⚡ 909000020 (devil move)\n[FFFFFF]⚡ 909000008 (shoot dance)\n[FFFFFF]⚡ 909000006 (chicken)\n[00FFFF]━━━━━━━━━━━━[FFD3EF]\n"
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                            
                            EM = await FS(key , iv)
                            await SEndPacKeT(whisper_writer , online_writer , 'OnLine' , EM)
                            
                            # SUCCESS MESSAGE
                            success_message = f"[C][B][FFD700]═══⚓︎ EMOTE IDS MENU 2/2 ⚓︎═══[FFD3EF]\n[FFFFFF]⚡ 909000014 (THRONE)\n[FFFFFF]⚡ 909000010 (rose)\n[FFFFFF]⚡ 909038004 (heart)\n[FFFFFF]⚡ 909034001 (book)\n[FFFFFF]⚡ 909049017 (guild flag\n[FFFFFF]⚡ 909040004 (fish\n[FFFFFF]⚡ 909041003 (inosuke\n[FFFFFF]⚡ 909041012(grmaster)\n[00FFFF]━━━━━━━━━━━━[FFD3EF]\n"
                            await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                        if inPuTMsG.strip().startswith('/fs'):
                            parts = inPuTMsG.strip().split()
                            
                            # 1. Kiểm tra cú pháp
                            if len(parts) < 2:
                                usage_msg = f"[B][C][FF0000]❌ Usage: /fs <TeamCode>\n"
                                await safe_send_message(response.Data.chat_type, usage_msg, uid, chat_id, key, iv)
                                return
                            
                            team_code = parts[1]
                            SPAM_COUNT = 30
                            DELAY_PER_PACKET = 0.2 #delay
                            
                            try:
                                # BƯỚC 1: Thông báo và Join Team
                                await safe_send_message(response.Data.chat_type, f"[B][C][FFA500]🚀 Joining {team_code}...\n", uid, chat_id, key, iv)
                                
                                # Tạo gói tin Join Team (Sử dụng GenJoinSquadsPacket đã có trong bot cũ)
                                join_pkt = await GenJoinSquadsPacket(team_code, key, iv)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', join_pkt)
                                
                                # BƯỚC 2: Đợi 2 giây để bot vào phòng
                                await asyncio.sleep(1.0)
                                
                                # BƯỚC 3: Tạo gói tin Start (Sử dụng hàm FS đã có)
                                start_pkt = await FS(key, iv)
                                
                                if start_pkt:
                                    await safe_send_message(response.Data.chat_type, f"[B][C][FF0000]⚡ Spamming START ({SPAM_COUNT}x)...\n", uid, chat_id, key, iv)
                                    
                                    # Vòng lặp Spam
                                    for _ in range(SPAM_COUNT):
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', start_pkt)
                                        await asyncio.sleep(DELAY_PER_PACKET) # Chờ 0.15 giây
                                    
                                    # BƯỚC 4: Thoát Team (Sử dụng ExiT đã có)
                                    await asyncio.sleep(0.5) # Delay an toàn trước khi Leave
                                    leave_pkt = await ExiT(None, key, iv)
                                    
                                    # Kiểm tra Writer trước khi gửi Leave (khắc phục lỗi NoneType)
                                    if online_writer:
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', leave_pkt)
                                        final_msg = f"[B][C][00FF00]✅ Force Start Finished & Left Team.\n"
                                    else:
                                        final_msg = f"[B][C][00FF00]✅ Force Start Finished. Connection lost, cannot send Leave packet.\n"

                                    await safe_send_message(response.Data.chat_type, final_msg, uid, chat_id, key, iv)

                                else:
                                    await safe_send_message(response.Data.chat_type, f"[B][C][FF0000]❌ Error creating start packet.\n", uid, chat_id, key, iv)

                            except Exception as e:
                                # Bắt lỗi chung
                                print(f"Force start error: {e}")
                                await safe_send_message(response.Data.chat_type, f"[B][C][FF0000]❌ Error: {e}\n", uid, chat_id, key, iv)
                        # attack COMMAND - Lag trong 5s rồi vô trận
# TEST COMMAND - Lag trong 5s rồi vào trận & thoát
                        # ATTACK COMMAND - Lag trong 5s rồi vào trận & thoát
                        if inPuTMsG.strip().startswith('/attack '):
                            print('Processing /attack command')
                        
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /attack (team_code)\nExample: /attack ABC123\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                team_code = parts[1]
                        
                                # Stop lag cũ nếu có
                                if lag_task and not lag_task.done():
                                    lag_running = False
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)
                        
                                # Start lag mới
                                lag_running = True
                                lag_task = asyncio.create_task(lag_team_loop(team_code, key, iv, region))
                        
                                start_msg = f"[B][C][FFFF00]⚠ ATTACK STARTED!\nLag running for 5s, then match will be forced..."
                                await safe_send_message(response.Data.chat_type, start_msg, uid, chat_id, key, iv)
                        
                                # Chạy lag 5s
                                await asyncio.sleep(5)
                        
                                # Gửi lệnh vô trận TRƯỚC khi dừng lag (10 lần)
                                match_sent = False
                                for i in range(10):
                                    try:
                                        EM = await FS(key, iv)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', EM)
                                        print(f"[ATTACK] Match start packet #{i + 1} sent successfully.")
                                        match_sent = True
                                        await asyncio.sleep(0.05)
                                    except Exception as e:
                                        print(f"[ATTACK] Error sending match start #{i + 1}: {e}")
                                        await asyncio.sleep(0.05)
                        
                                # Dừng lag
                                lag_running = False
                                if lag_task and not lag_task.done():
                                    lag_task.cancel()
                                    await asyncio.sleep(0.1)
                        
                                # Thoát squad sau khi vào trận
                                try:
                                    exit_packet = await ExiT(None, key, iv)
                                    await SEndPacKeT(whisper_writer, online_writer, 'OnLine', exit_packet)
                                    print("[ATTACK] Squad exit packet sent successfully.")
                                except Exception as e:
                                    print(f"[ATTACK] Error sending exit packet: {e}")
                        
                                # Gửi kết quả
                                if match_sent:
                                    success_msg = (
                                        f"[B][C][00FF00]🎮 ATTACK COMPLETED!\n"
                                        f"Team: {team_code}\n"
                                        f"⏱ Lag: 5s\n"
                                        f"🚀 Match start: **SENT x10**\n"
                                        f"🚪 Squad exit: DONE\n"
                                    )
                                else:
                                    success_msg = (
                                        f"[B][C][FF0000]⚠ ATTACK FAILED!\n"
                                        f"Không thể gửi lệnh vào trận!\n"
                                        f"Có thể writer đã mất kết nối hoặc FS sai.\n"
                                    )
                        
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)


# STOP ATTACK (nếu muốn)
                        if inPuTMsG.strip() == '/stop attack':
                            lag_running = False
                        
                            if lag_task and not lag_task.done():
                                lag_task.cancel()
                        
                            try:
                                if lag_task:
                                    await lag_task
                            except:
                                pass
                        
                            msg = f"[B][C][FFD3EF]🛑 ATTACK FORCE STOPPED!\n"
                            await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)


                        
                        
                        # STOP attack MANUALLY (optional)
                        if inPuTMsG.strip() == '/stop attack':
                            lag_running = False
                        
                            if lag_task and not lag_task.done():
                                lag_task.cancel()
                        
                            try:
                                if lag_task: await lag_task
                            except:
                                pass
                        
                            msg = f"[B][C][FFD3EF]🛑 ATTACK FORCE STOPPED!\n"
                            await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
    
                        # Emote command - works in all chat types
                        if inPuTMsG.strip().startswith('/em '):
                            print(f'Processing simple EMOTE_MAP_2 command in chat type: {response.Data.chat_type}')
                            
                            # Đặt số lượng emote tối đa trong EMOTE_MAP_2 (Dùng để kiểm tra phạm vi)
                            MAX_EMOTE_NUMBER = 417 # Thay đổi số này theo kích thước EMOTE_MAP_2 của bạn
                            
                            parts = inPuTMsG.strip().split()
                            # Cần ít nhất 2 phần (lệnh /em, 1 UID, và 1 số emote)
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /em uid1 [uid2] [uid3] [uid4] number(1-{MAX_EMOTE_NUMBER})\nExample: /em 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                                
                            initial_message = f'[B][C]{get_random_color()}\nSending indexed emote to target(s)...\n'
                            await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)

                            target_uids = []
                            s = False # Biến cờ cho lỗi
                            
                            try:
                                # Phần tử cuối cùng phải là số thứ tự emote (index)
                                emote_index = int(parts[-1])
                                
                                # Kiểm tra phạm vi index
                                if not (1 <= emote_index <= MAX_EMOTE_NUMBER):
                                    raise ValueError(f"Emote number must be between 1 and {MAX_EMOTE_NUMBER}")

                                # Tra cứu Emote ID từ EMOTE_MAP_2
                                emote_id = EMOTE_MAP_2.get(emote_index)
                                if emote_id is None:
                                    raise ValueError(f"Emote number {emote_index} not found in EMOTE_MAP_2.")

                                # Các phần còn lại là UID mục tiêu
                                for part in parts[1:-1]:
                                    target_uids.append(int(part))

                                if not target_uids:
                                    raise ValueError("No valid UIDs provided.")

                            except ValueError as ve:
                                print("ValueError:", ve)
                                s = True
                                error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format/range: {str(ve)}\nUsage: /em uid1 [uid2] ... number(1-{MAX_EMOTE_NUMBER})\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            except Exception as e:
                                print(f"Error parsing emote command: {e}")
                                s = True
                                error_msg = f"[B][C][FF0000]❌ ERROR! An unknown error occurred: {str(e)}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                            # Nếu không có lỗi khi phân tích
                            if not s:
                                try:
                                    # Gửi emote đến từng UID
                                    for target in target_uids:
                                        H = await Emote_k(target, emote_id, key, iv, region)
                                        await SEndPacKeT(whisper_writer, online_writer, 'OnLine', H)
                                        await asyncio.sleep(0.1)
                                    
                                    # SUCCESS MESSAGE
                                    targets_str = ', '.join(map(str, target_uids))
                                    success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Emote {emote_index} (ID: {emote_id}) sent to {len(target_uids)} player(s)!\nTargets: {targets_str}\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR sending emote: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Fast emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/fem'):
                            print('Processing fast emote spam using EMOTE_MAP_2 in any chat type')
                            
                            # Đặt số lượng emote tối đa trong EMOTE_MAP_2
                            MAX_EMOTE_NUMBER_2 = 417 # Thay đổi số này theo kích thước EMOTE_MAP_2 thực tế
                            
                            parts = inPuTMsG.strip().split()
                            # Cần ít nhất 2 phần (lệnh /fem, 1 UID, và 1 số emote)
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /fem uid1 [uid2] [uid3] [uid4] number(1-{MAX_EMOTE_NUMBER_2})\nVí dụ: /fem 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                continue
                            
                            uids = []
                            emote_index = None
                            emote_id = None
                            s = False

                            try:
                                # Phần tử cuối cùng phải là số thứ tự emote (index)
                                if parts[-1].isdigit():
                                    emote_index = int(parts[-1])
                                else:
                                    raise ValueError("Emote number not found or invalid format.")
                                
                                # Kiểm tra phạm vi index
                                if not (1 <= emote_index <= MAX_EMOTE_NUMBER_2):
                                    raise ValueError(f"Emote number must be between 1 and {MAX_EMOTE_NUMBER_2}.")

                                # Tra cứu Emote ID từ EMOTE_MAP_2
                                emote_id = EMOTE_MAP_2.get(emote_index)
                                if emote_id is None:
                                    raise ValueError(f"Emote number {emote_index} not found in EMOTE_MAP_2.")

                                # Các phần còn lại là UID mục tiêu
                                for part in parts[1:-1]:
                                    if part.isdigit():
                                        uids.append(part)
                                    else:
                                        print(f"Warning: Skipping non-numeric part in UID list: {part}")

                                if not uids:
                                    raise ValueError("No valid UIDs provided.")

                            except ValueError as ve:
                                print("ValueError:", ve)
                                s = True
                                error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format/range: {str(ve)}\nUsage: /fem uid1 [uid2] ... number(1-{MAX_EMOTE_NUMBER_2})\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            except Exception as e:
                                print(f"Error parsing fast emote command: {e}")
                                s = True
                                error_msg = f"[B][C][FF0000]❌ ERROR! An unknown error occurred: {str(e)}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            
                            # Nếu không có lỗi khi phân tích
                            if not s:
                                try:
                                    # Stop any existing fast spam
                                    if 'fast_spam_task' in locals() and fast_spam_task and not fast_spam_task.done():
                                        fast_spam_running = False
                                        fast_spam_task.cancel()
                                    
                                    # Start new fast spam
                                    fast_spam_running = True
                                    
                                    # Chú ý: fast_emote_spam cần nhận Emote ID (string)
                                    fast_spam_task = asyncio.create_task(fast_emote_spam(uids, str(emote_id), key, iv, region))
                                    
                                    # SUCCESS MESSAGE
                                    targets_str = ', '.join(uids)
                                    success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Fast emote spam started!\nEmote Index: {emote_index} (ID: {emote_id})\nTargets: {len(uids)} players ({targets_str})\nSpam count: 25 times\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)

                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR starting fast spam: {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        # Custom emote spam command - works in all chat types
                        if inPuTMsG.strip().startswith('/cem'):
                            print('Processing custom emote spam using EMOTE_MAP_2 in any chat type')
                            
                            # Đặt số lượng emote tối đa trong EMOTE_MAP_2
                            MAX_EMOTE_NUMBER_2 = 417 # Cần đồng bộ với lệnh /fem
                            
                            parts = inPuTMsG.strip().split()
                            # Cần ít nhất 4 phần (lệnh /cem, 1 UID, 1 số emote, 1 số lần)
                            if len(parts) < 4:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /cem (uid) number(1-{MAX_EMOTE_NUMBER_2}) (times)\nExample: /cem 123456789 1 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    # target_uid: parts[1]
                                    # emote_index: parts[2]
                                    # times: parts[3]
                                    
                                    target_uid = parts[1] # Chỉ hỗ trợ 1 UID duy nhất như logic cũ
                                    emote_index = int(parts[2])
                                    times = int(parts[3])
                                    
                                    # Kiểm tra phạm vi index
                                    if not (1 <= emote_index <= MAX_EMOTE_NUMBER_2):
                                        raise ValueError(f"Emote number must be between 1 and {MAX_EMOTE_NUMBER_2}!")

                                    # Tra cứu Emote ID từ EMOTE_MAP_2
                                    emote_id = EMOTE_MAP_2.get(emote_index)
                                    if emote_id is None:
                                        raise ValueError(f"Emote number {emote_index} not found in EMOTE_MAP_2!")
                                    
                                    if times <= 0:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Times must be greater than 0!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    elif times > 100:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Maximum 100 times allowed for safety!\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    else:
                                        # Stop any existing custom spam
                                        if 'custom_spam_task' in locals() and custom_spam_task and not custom_spam_task.done():
                                            custom_spam_running = False
                                            custom_spam_task.cancel()
                                            await asyncio.sleep(0.5)
                                        
                                        # Start new custom spam
                                        custom_spam_running = True
                                        # Chú ý: custom_emote_spam cần nhận Emote ID (string)
                                        custom_spam_task = asyncio.create_task(custom_emote_spam(target_uid, str(emote_id), times, key, iv, region))
                                        
                                        # SUCCESS MESSAGE
                                        success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Custom emote spam started!\nTarget: {target_uid}\nEmote Index: {emote_index} (ID: {emote_id})\nTimes: {times}\n"
                                        await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        
                                except ValueError as ve:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format: {str(ve)}\nUsage: /cem (uid) number(1-{MAX_EMOTE_NUMBER_2}) (times)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Spam request command - works in all chat types
                        if inPuTMsG.strip().startswith('/spm'):
                            print('Processing spam request in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /spm_inv (uid)\nExample: /spm_inv 123456789\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                try:
                                    target_uid = parts[1]
                                    
                                    # Stop any existing spam request
                                    if spam_request_task and not spam_request_task.done():
                                        spam_request_running = False
                                        spam_request_task.cancel()
                                        await asyncio.sleep(0.5)
                                    
                                    # Start new spam request
                                    spam_request_running = True
                                    spam_request_task = asyncio.create_task(spam_request_loop(target_uid, key, iv, region))
                                    
                                    # SUCCESS MESSAGE
                                    success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Spam request started!\nTarget: {target_uid}\nRequests: 30\nSpeed: Fast\n"
                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                        
                                except Exception as e:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! {str(e)}\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Stop spam request command - works in all chat types
                        if inPuTMsG.strip() == '/sspm':
                            if spam_request_task and not spam_request_task.done():
                                spam_request_running = False
                                spam_request_task.cancel()
                                success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Spam request stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active spam request to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW EVO COMMAND
                        if inPuTMsG.strip().startswith('/ibg'):
                            print('Processing /ibg command')
                        
                            try:
                                # Lấy UID cần mời -> Nếu không nhập thì mời chính người gửi lệnh
                                parts = inPuTMsG.strip().split()
                                if len(parts) >= 2:
                                    target_uid = parts[1]
                                else:
                                    target_uid = uid  # UID của người gửi lệnh
                        
                                initial_message = f"[B][C]{get_random_color()}\n\n🔁 Đang mời bạn vào nhóm của tôi vui lòng chấp nhận...\n\n"
                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                        
                                # Gửi packet mời vào group hiện tại
                                V = await SEnd_InV(5, target_uid, key, iv, region)  # 5 = Squad type (giữ nguyên như /5)
                                await asyncio.sleep(0.3)
                                await SEndPacKeT(whisper_writer, online_writer, 'OnLine', V)
                        
                                # Thông báo thành công
                                success_message = f"[B][C][FFD3EF]🎉 Thành công! Đã gửi lời mời tới id {target_uid} vào đội của tôi!\n"
                                await safe_send_message(response.Data.chat_type, success_message, uid, chat_id, key, iv)
                        
                            except Exception as e:
                                error_msg = f"[B][C][FF0000]❌ ERROR! {str(e)}\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)


        
                        if inPuTMsG.strip().startswith('/evo '):
                            print('Processing evo command in any chat type')
                        
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ Lỗi! Dùng: /evo uid1 [uid2] [uid3] [uid4] number(1-21), 'all' hoặc 'random'\nVí d️ụ: /evo 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse UIDs và chế độ
                                uids = []
                                mode = None  # number, "all", hoặc "random"
                        
                                for part in parts[1:]:
                                    if part.isdigit() and 1 <= int(part) <= 21:
                                        mode = int(part)
                                    elif part.lower() in ["all", "random"]:
                                        mode = part.lower()
                                    else:
                                        uids.append(part)
                        
                                if not uids or mode is None:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Format không hợp lệ! Usage: /evo uid1 [uid2] [uid3] [uid4] number(1-21), 'all' hoặc 'random'\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        # --- MODE "ALL" ---
                                        if mode == "all":
                                            for num in range(1, 21):
                                                await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                                await evo_emote_spam(uids, num, key, iv, region)
                                                await asyncio.sleep(7.5)  # nhịp 2.5 giây
                                            success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Finished sending all 21 emotes.\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                        
                                        # --- MODE "RANDOM" ---
                                        elif mode == "random":
                                            # Tạo danh sách emote riêng cho từng UID
                                            uid_emote_map = {}
                                            for u in uids:
                                                emotes_list = list(range(1, 22))
                                                random.shuffle(emotes_list)
                                                uid_emote_map[u] = emotes_list
                        
                                            # Gửi emote theo nhịp cho tất cả UID
                                            for i in range(21):
                                                for u in uids:
                                                    num = uid_emote_map[u][i]
                                                    await safe_send_message(response.Data.chat_type, msg, uid, chat_id, key, iv)
                                                    await evo_emote_spam([u], num, key, iv, region)
                                                await asyncio.sleep(7.5)
                                            success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Finished sending 21 random emotes to all UIDs.\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                        
                                        # --- MODE SỐ CỤ THỂ ---
                                        else:
                                            if mode not in EMOTE_MAP:
                                                error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                            else:
                                                initial_message = f"[B][C]{get_random_color()}\nSending evolution emote {mode}...\n"
                                                await safe_send_message(response.Data.chat_type, initial_message, uid, chat_id, key, iv)
                        
                                                success, result_msg = await evo_emote_spam(uids, mode, key, iv, region)
                        
                                                if success:
                                                    success_msg = f"[B][C][FFD3EF]✅ SUCCESS! {result_msg}\n"
                                                    await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                                else:
                                                    error_msg = f"[B][C][FF0000]❌ ERROR! {result_msg}\n"
                                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                    except Exception as e:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! {str(e)}\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                        



                        if inPuTMsG.strip().startswith('/ef '):
                            print('Processing evo_fast command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 2:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)\nExample: /evo_fast 123456789 1\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids and number
                                uids = []
                                number = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number should be 1-21 (1 or 2 digits)
                                            number = part
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                if not number and parts[-1].isdigit() and len(parts[-1]) <= 2:
                                    number = parts[-1]
                                
                                if not uids or not number:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo_fast uid1 [uid2] [uid3] [uid4] number(1-21)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_fast spam
                                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                                evo_fast_spam_running = False
                                                evo_fast_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_fast spam
                                            evo_fast_spam_running = True
                                            evo_fast_spam_task = asyncio.create_task(evo_fast_emote_spam(uids, number_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Fast evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nSpam count: 25 times\nInterval: 0.1 seconds\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number format! Use 1-21 only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # NEW EVO_CUSTOM COMMAND
                        if inPuTMsG.strip().startswith('/ec '):
                            print('Processing evo_c command in any chat type')
                            
                            parts = inPuTMsG.strip().split()
                            if len(parts) < 3:
                                error_msg = f"[B][C][FF0000]❌ ERROR! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-21) time(1-100)\nExample: /evo_c 123456789 1 10\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                            else:
                                # Parse uids, number, and time
                                uids = []
                                number = None
                                time_val = None
                                
                                for part in parts[1:]:
                                    if part.isdigit():
                                        if len(part) <= 2:  # Number or time should be 1-100 (1, 2, or 3 digits)
                                            if number is None:
                                                number = part
                                            elif time_val is None:
                                                time_val = part
                                            else:
                                                uids.append(part)
                                        else:
                                            uids.append(part)
                                    else:
                                        break
                                
                                # If we still don't have time_val, try to get it from the last part
                                if not time_val and len(parts) >= 3:
                                    last_part = parts[-1]
                                    if last_part.isdigit() and len(last_part) <= 3:
                                        time_val = last_part
                                        # Remove time_val from uids if it was added by mistake
                                        if time_val in uids:
                                            uids.remove(time_val)
                                
                                if not uids or not number or not time_val:
                                    error_msg = f"[B][C][FF0000]❌ ERROR! Invalid format! Usage: /evo_c uid1 [uid2] [uid3] [uid4] number(1-21) time(1-100)\n"
                                    await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                else:
                                    try:
                                        number_int = int(number)
                                        time_int = int(time_val)
                                        
                                        if number_int not in EMOTE_MAP:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Number must be between 1-21 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        elif time_int < 1 or time_int > 100:
                                            error_msg = f"[B][C][FF0000]❌ ERROR! Time must be between 1-100 only!\n"
                                            await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)
                                        else:
                                            # Stop any existing evo_custom spam
                                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                                evo_custom_spam_running = False
                                                evo_custom_spam_task.cancel()
                                                await asyncio.sleep(0.5)
                                            
                                            # Start new evo_custom spam
                                            evo_custom_spam_running = True
                                            evo_custom_spam_task = asyncio.create_task(evo_custom_emote_spam(uids, number_int, time_int, key, iv, region))
                                            
                                            # SUCCESS MESSAGE
                                            emote_id = EMOTE_MAP[number_int]
                                            success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Custom evolution emote spam started!\nTargets: {len(uids)} players\nEmote: {number_int} (ID: {emote_id})\nRepeat: {time_int} times\nInterval: 0.1 seconds\n"
                                            await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                                            
                                    except ValueError:
                                        error_msg = f"[B][C][FF0000]❌ ERROR! Invalid number/time format! Use numbers only.\n"
                                        await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Stop evo_fast spam command
                        if inPuTMsG.strip() == '/stop ef':
                            if evo_fast_spam_task and not evo_fast_spam_task.done():
                                evo_fast_spam_running = False
                                evo_fast_spam_task.cancel()
                                success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Evolution fast spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution fast spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        # Stop evo_custom spam command
                        if inPuTMsG.strip() == '/stop ec':
                            if evo_custom_spam_task and not evo_custom_spam_task.done():
                                evo_custom_spam_running = False
                                evo_custom_spam_task.cancel()
                                success_msg = f"[B][C][FFD3EF]✅ SUCCESS! Evolution custom spam stopped successfully!\n"
                                await safe_send_message(response.Data.chat_type, success_msg, uid, chat_id, key, iv)
                            else:
                                error_msg = f"[B][C][FF0000]❌ ERROR! No active evolution custom spam to stop!\n"
                                await safe_send_message(response.Data.chat_type, error_msg, uid, chat_id, key, iv)

                        if inPuTMsG.strip().lower() == "/emenu":
                            print(f"Lệnh /emenu đã được gọi bởi: {uid} Loại chat: {response.Data.chat_type}")
                        
                            # Danh sách màu HEX hợp lệ
                            colors = ["FF0000","00FF00","0000FF","FFFF00","FF00FF","00FFFF","FFA500","008000","800080","000080",
                                      "808000","FF4500","32CD32","1E90FF","8A2BE2","FF1493","ADFF2F","FF8C00","FF6347","40E0D0",
                                      "7FFF00","DA70D6","00FA9A","FF69B4","4682B4","9400D3","FFC0CB"]
                        
                            # Hàm lấy màu ngẫu nhiên không trùng nhau
                            def get_random_colors(n):
                                return random.sample(colors, n)
                        
                            # --- Menu 1 ---
                            colors1 = get_random_colors(5)
                            menu1 = f'''[C][B][FFD700]══Nguyễn Tiêu | Extra Menu 1═══[FFFF00]
                        [FFD700]════Chức năng 1════[FFFF00]
                        [{colors1[0]}]01.⚡Cúp FFWC → /a1
                        [{colors1[1]}]02.⚡Tặng hoa → /a2  
                        [{colors1[2]}]03.⚡ → a/3
                        [{colors1[3]}]04.⚡Chưa có chức năng → a/4
                        [{colors1[4]}]05.⚡Chưa có chức năng → a/5
                        [FFD3EF]━━━━━━━━━━━━[FFFF00]'''
                            await safe_send_message(response.Data.chat_type, menu1, uid, chat_id, key, iv)
                            await asyncio.sleep(0.5)
                        
                            # --- Menu 2 ---
                            colors2 = get_random_colors(5)
                            menu2 = f'''[C][B][FFD700]══Nguyễn Tiêu | Extra Menu 2═══[FFFF00]
                        [FFD700]════Chức năng 2════[FFFF00]
                        [{colors2[0]}]06.⚡Chưa có chức năng → N/A
                        [{colors2[1]}]07.⚡Chưa có chức năng → N/A
                        [{colors2[2]}]08.⚡Chưa có chức năng → N/A
                        [{colors2[3]}]09.⚡Chưa có chức năng → N/A
                        [{colors2[4]}]10.⚡Chưa có chức năng → N/A
                        [FFD3EF]━━━━━━━━━━━━[FFFF00]'''
                            await safe_send_message(response.Data.chat_type, menu2, uid, chat_id, key, iv)
                            await asyncio.sleep(0.5)
                        
                            # --- Menu 3 ---
                            colors3 = get_random_colors(5)
                            menu3 = f'''[C][B][FFD700]══Nguyễn Tiêu | Extra Menu 3═══[FFFF00]
                        [FFD700]════Chức năng 3════[FFFF00]
                        [{colors3[0]}]11.⚡Chưa có chức năng → N/A
                        [{colors3[1]}]12.⚡Chưa có chức năng → N/A
                        [{colors3[2]}]13.⚡Chưa có chức năng → N/A
                        [{colors3[3]}]14.⚡Chưa có chức năng → N/A
                        [{colors3[4]}]15.⚡Chưa có chức năng → N/A
                        [FFD3EF]━━━━━━━━━━━━[FFFF00]'''
                            await safe_send_message(response.Data.chat_type, menu3, uid, chat_id, key, iv)
                            await asyncio.sleep(0.5)
                        
                            # --- Menu 4 ---
                            colors4 = get_random_colors(5)
                            menu4 = f'''[C][B][FFD700]══Nguyễn Tiêu | Extra Menu 4═══[FFFF00]
                        [FFD700]════Chức năng 4════[FFFF00]
                        [{colors4[0]}]16.⚡Chưa có chức năng → N/A
                        [{colors4[1]}]17.⚡Chưa có chức năng → N/A
                        [{colors4[2]}]18.⚡Chưa có chức năng → N/A
                        [{colors4[3]}]19.⚡Chưa có chức năng → N/A
                        [{colors4[4]}]20.⚡Chưa có chức năng → N/A
                        [FFD3EF]━━━━━━━━━━━━[FFFF00]'''
                            await safe_send_message(response.Data.chat_type, menu4, uid, chat_id, key, iv)
                            await asyncio.sleep(0.5)
                        
                            # --- Menu 5 ---
                            colors5 = get_random_colors(5)
                            menu5 = f'''[C][B][FFD700]══Nguyễn Tiêu | Extra Menu 5═══[FFFF00]
                        [FFD700]════Chức năng 5════[FFFF00]
                        [{colors5[0]}]21.⚡Chưa có chức năng → N/A
                        [{colors5[1]}]22.⚡Chưa có chức năng → N/A
                        [{colors5[2]}]23.⚡Chưa có chức năng → N/A
                        [{colors5[3]}]24.⚡Chưa có chức năng → N/A
                        [{colors5[4]}]25.⚡Chưa có chức năng → N/A
                        [FFD3EF]━━━━━━━━━━━━[FFFF00]'''
                            await safe_send_message(response.Data.chat_type, menu5, uid, chat_id, key, iv)
                        
    
                        # FIXED HELP MENU SYSTEM - Now detects commands properly
                        if inPuTMsG.strip().lower() == "/help":
                            print(f"Lệnh /help đã được gọi bởi: {uid} Loại chat: {response.Data.chat_type}")
                        
                            colors = ["[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFA500]", "[FFC0CB]"]
                        
                            def rc():
                                return random.choice(colors)
                        
                            menu1 = f'''[C][B][FFD700]══Nguyễn Tiêu | Help 1/4═══
[FFD700]════Lệnh cơ bản════
{rc()}01.⚡Xem thông tin quân đoàn
{rc()}/clan [ID]
{rc()}02.⚡Tạo team 5
{rc()}/5
{rc()}03.⚡Tạo team 6
{rc()}/6
{rc()}04.⚡Tạo team 3
{rc()}/3
{rc()}05.⚡Mời bot vào team
{rc()}/join [TeamCode]
{rc()}06.⚡Mời bạn vào team bot
{rc()}/ibg
[FFD3EF]━━━━━━━━━━━━'''
                        
                            await send_menu(response.Data.chat_type, menu1, uid, chat_id, key, iv)
                        
                            menu2 = f'''[C][B][FFD700]══Nguyễn Tiêu | Help 2/4═══
[FFD700]════Lệnh nâng cao════
{rc()}07.⚡Tăng tốc bot
{rc()}/boost
{rc()}08.⚡Thoát bot khỏi team
{rc()}/exit
{rc()}09.⚡Xem thông tin người chơi
{rc()}/info [ID]
{rc()}10.⚡Chat với AI (EN)
{rc()}/ai [câu hỏi]
{rc()}11.⚡Thông tin người tạo bot
{rc()}/dev
[FFD3EF]━━━━━━━━━━━━'''
                        
                            await send_menu(response.Data.chat_type, menu2, uid, chat_id, key, iv)
                        
                            menu3 = f'''[C][B][FFD700]══Nguyễn Tiêu | Help 3/4═══
[FFD700]════Lệnh hành động════
{rc()}12.⚡Dùng hành động
{rc()}/em [ID]
{rc()}13.⚡Spam hành động
{rc()}/fem [ID]
{rc()}14.⚡Spam hành động theo số lần
{rc()}/cem [ID] [Số lần]
{rc()}15.⚡Hành động súng nâng cấp
{rc()}/evo [ID] [1-21/all/random]
{rc()}16.⚡Spam súng nâng cấp
{rc()}/fe [ID] [1-21]
{rc()}17.⚡Spam súng nâng cấp theo số lần
{rc()}/ec [ID] [1-21] [Số lần]
[FFD3EF]━━━━━━━━━━━━'''
                        
                            await send_menu(response.Data.chat_type, menu3, uid, chat_id, key, iv)
                        
                            menu4 = f'''[C][B][FFD700]══Nguyễn Tiêu | Help 4/4══
[FFD700]════Lệnh Troll════
{rc()}18.⚡Spam lời mời vào team
{rc()}/spm [ID] | /sspm
{rc()}19.⚡Spam lag
{rc()}/lag [TeamCode] | /stop lag
{rc()}20.⚡Ép cả đội vào trận
{rc()}/fs [TeamCode]
{rc()}21.⚡Tấn công đội
{rc()}/attack [TeamCode] | /stop attack
[FFD3EF]━━━━━━━━━━━━'''
                        
                            await send_menu(response.Data.chat_type, menu4, uid, chat_id, key, iv)
                        
                            menu5 = f'''[C][B]{rc()}Tiktok:@nguyentieulive
                        
{rc()}Facebook: Nguyễn Tiêu'''
                        
                            await safe_send_message(response.Data.chat_type, menu5, uid, chat_id, key, iv)

            whisper_writer.close() ; await whisper_writer.wait_closed() ; whisper_writer = None
                    
                    	
                    	
        except Exception as e: print(f"ErroR {ip}:{port} - {e}") ; whisper_writer = None
        await asyncio.sleep(reconnect_delay)

async def MaiiiinE(Uid, Pw):
    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id or not access_token:
        print(f"Bot lỗi không tìm thấy tài khoản {Uid}")
        return None

    PyL = await EncRypTMajoRLoGin(open_id, access_token)
    MajoRLoGinResPonsE = await MajorLogin(PyL)
    if not MajoRLoGinResPonsE:
        print(f"Tài khoản {Uid} => Đã bị band hoặc chưa được tạo!")
        return None

    MajoRLoGinauTh = await DecRypTMajoRLoGin(MajoRLoGinResPonsE)
    UrL = MajoRLoGinauTh.url
    print(UrL)
    region = MajoRLoGinauTh.region

    ToKen = MajoRLoGinauTh.token
    TarGeT = MajoRLoGinauTh.account_uid
    key = MajoRLoGinauTh.key
    iv = MajoRLoGinauTh.iv
    timestamp = MajoRLoGinauTh.timestamp

    LoGinDaTa = await GetLoginData(UrL, PyL, ToKen)
    if not LoGinDaTa:
        print(f"Bot lỗi - Nhận cổng từ thông tin đăng nhập của {Uid}!")
        return None

    LoGinDaTaUncRypTinG = await DecRypTLoGinDaTa(LoGinDaTa)
    OnLinePorTs = LoGinDaTaUncRypTinG.Online_IP_Port
    ChaTPorTs = LoGinDaTaUncRypTinG.AccountIP_Port
    OnLineiP, OnLineporT = OnLinePorTs.split(":")
    ChaTiP, ChaTporT = ChaTPorTs.split(":")
    acc_name = LoGinDaTaUncRypTinG.AccountName

    print(ToKen)
    equie_emote(ToKen, UrL)
    AutHToKen = await xAuThSTarTuP(int(TarGeT), ToKen, int(timestamp), key, iv)
    ready_event = asyncio.Event()

    task1 = asyncio.create_task(TcPChaT(ChaTiP, ChaTporT, AutHToKen, key, iv, LoGinDaTaUncRypTinG, ready_event, region))
    await ready_event.wait()
    await asyncio.sleep(1)
    task2 = asyncio.create_task(TcPOnLine(OnLineiP, OnLineporT, key, iv, AutHToKen))
    os.system('clear')
    print(render('BotTCP', colors=['white', 'red'], align='center'))
    print(f"\n - Bot đang chạy trên id : {TarGeT} | Tên acc bot : {acc_name}")
    print(f" - Trạng thái bot > Tốt | Online !")
    await asyncio.gather(task1, task2)

# --- Hàm chính chạy tất cả bot ---
async def StarTinG():
    # Đọc file bot.txt
    try:
        with open("bot.txt", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Bot lỗi - Không tìm thấy file bot.txt!")
        return
    except json.JSONDecodeError:
        print("Bot lỗi - bot.txt không phải JSON hợp lệ!")
        return

    # Chạy tuần tự từng bot
    for Uid, Pw in data.items():
        while True:
            try:
                await asyncio.wait_for(MaiiiinE(Uid, Pw), timeout=7*60*60)
            except asyncio.TimeoutError:
                print(f"Token của {Uid} đã hết hạn! Khởi động lại bot...")
            except Exception as e:
                print(f"Bot lỗi {Uid} - {e} => Đang khởi động lại ...")

if __name__ == '__main__':
    asyncio.run(StarTinG())
