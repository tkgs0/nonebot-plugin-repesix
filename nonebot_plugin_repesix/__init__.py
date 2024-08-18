from random import random
from nonebot import on_regex, on_fullmatch
from nonebot.plugin import PluginMetadata
from nonebot.internal.adapter import Event


__plugin_meta__ = PluginMetadata(
    name="复读6",
    description="当有人发送 `6` 或 `主|蚌|蜯|草|艹|乐|樂|寄|典|孝|急|麻` 时概率触发复读",
    usage="概率公示: random()*10//1 == 6.0",
    type="application",
    homepage="https://github.com/tkgs0/nonebot-plugin-repesix",
    supported_adapters=None
)


six = on_regex(r"^6+$", priority=5, block=False)

@six.handle()
async def _(event: Event):
    if random()*10//1 == 6.0:
        await six.finish(event.get_message())


nonsense = on_fullmatch(
    ("主", "蚌", "蜯", "草", "艹", "乐", "樂", "寄", "典", "孝", "急", "麻"),
    priority=5,
    block=False
)

@nonsense.handle()
async def _(event: Event):
    if random()*10//1 == 6.0:
        await nonsense.finish(event.get_message())
