---
title: TTS 语音合成配置
created: 2026-04-19
updated: 2026-04-19
type: config
tags: [tts, voice, edge-tts, minimax]
sources: []
---

# TTS 语音合成配置

## 默认配置：Edge TTS（本地）

**当前首选**，本地生成，额度无限。

```python
import asyncio, edge_tts

async def main():
    comm = edge_tts.Communicate("文本内容", "zh-CN-YunyangNeural")
    await comm.save("output.mp3")

asyncio.run(main())
```

### 中文音色列表（Edge TTS）

| ShortName | 风格 |
|---|---|
| `zh-CN-YunyangNeural` | 专业播音女声（当前默认）|
| `zh-CN-YiaoxiaoNeural` | 自然女声 |
| `zh-CN-XiaoyiNeural` | 自然女声 |
| `zh-CN-YunjianNeural` | 年轻男声 |
| `zh-CN-YunxiNeural` | 沉稳男声 |
| `zh-CN-YunxiaNeural` | 活泼女声 |
| `zh-CN-YunyangNeural` | 专业播音女声 |
| `zh-CN-liaoning-XiaobeiNeural` | 东北话 |
| `zh-HK-HiuGaaiNeural` | 粤语女声 |
| `zh-TW-HsiaoChenNeural` | 台湾女声 |
| `zh-TW-YunJheNeural` | 台湾男声 |
| `zh-CN-shaanxi-XiaoniNeural` | 陕西话 |

> 注意：Edge TTS 英文音色（如 en-US-AriaNeural）不支持中文，混用会导致中文数字逐位念。

## 备用：MiniMax 云端

额度有限，注意 usage limit，报 2056 错误说明用完了。

- **端点**：`https://api.minimaxi.com/v1/t2a_v2`
- **模型**：`speech-2.8-hd`（不是 `speech-02-hd`，后者报 2061 错误）
- **API Key**：在 `~/.hermes/.env` 中，`MINIMAX_CN_API_KEY`
- **注意**：国际端点 `api.minimax.io` 不认 CN key，会报 invalid api key
- **音频格式**：API 返回 hex 编码，解码用 `bytes.fromhex()`
- **可用音色**：female-yujie御姐、female-tianmei女、male-qn-qingse男清涩、chinese_male男

```python
import subprocess, json

r = subprocess.run(["bash", "-c",
    "grep MINIMAX_CN_API_KEY /home/xiong/.hermes/.env | tail -1 | cut -d= -f2"],
    capture_output=True, text=True)
key = r.stdout.strip()

payload = {
    "model": "speech-2.8-hd",
    "text": "文本",
    "stream": False,
    "voice_setting": {"voice_id": "female-yujie", "speed": 1.0, "volume": 1.0, "pitch": 0},
    "audio_setting": {"format": "mp3", "bitrate": 64000, "sample_rate": 32000}
}

data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
result = subprocess.run(
    ["curl", "-s", "-X", "POST", "https://api.minimaxi.com/v1/t2a_v2",
     "-H", f"Authorization: Bearer {key}",
     "-H", "Content-Type: application/json",
     "-d", data],
    capture_output=True
)

resp = json.loads(result.stdout)
audio_bytes = bytes.fromhex(resp["data"]["audio"])
with open("output.mp3", "wb") as f:
    f.write(audio_bytes)
```

## 发语音到 Telegram

chat_id: `1022202630`

```python
# 先生成音频
async def main():
    comm = edge_tts.Communicate("文本", "zh-CN-YunyangNeural")
    await comm.save("~/.hermes/audio_cache/tts.mp3")

# 用 send_message 发送
send_message(message="MEDIA:/path/to/tts.mp3", target="telegram")
```
