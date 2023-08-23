"""
{
    "allow-flight": [
        "布尔值",
        "允许玩家在安装添加飞行功能的mod前提下在生存模式下飞行。\n允许飞行可能会使恶意破坏者更加常见，因为此设定会使他们更容易达成目的。在创造模式下无作用。\nfalse - 不允许飞行。悬空超过5秒的玩家会被踢出服务器。\ntrue - 允许飞行。玩家得以使用任何能飞行的mod飞行。"
    ],
    "allow-nether": [
        "布尔值",
        "允许玩家进入下界。\nfalse - 下界传送门不会生效。\ntrue - 玩家可以通过下界传送门前往下界。"
    ],
    "broadcast-console-to-ops": [
        "布尔值",
        "向所有在线OP发送所执行命令的输出。"
    ],
    "broadcast-rcon-to-ops": [
        "布尔值",
        "向所有在线OP发送通过RCON执行的命令的输出。"
    ],
    "difficulty": [
        "字符串或数字",
        "定义服务器的游戏难度。\n如果设置了旧的数字ID，则会自动转化为英文的难度名称。\npeaceful (0) - 和平\neasy (1) - 简单\nnormal (2) - 普通\nhard (3) - 困难"
    ],
    "enable-command-block": [
        "布尔值",
        "是否启用命令方块。"
    ],
    "enable-jmx-monitoring": [
        "布尔值",
        "暴露一个具有对象名net.minecraft.server:type=Server的MBean和两个属性averageTickTime和tickTimes用于暴露以毫秒为单位的tick时间。"
    ],
    "enable-query": [
        "布尔值",
        "允许使用GameSpy4协议的服务器监听器。用于获取服务器信息。"
    ],
    "enable-rcon": [
        "布尔值",
        "是否允许远程访问服务器控制台。\n由于RCON协议传输数据时没有加密，所以不建议把RCON暴露在互联网上。RCON客户端和服务端交换的所有数据（包括RCON密码）都会泄露给正在监听此连接的人。"
    ],
    "enable-status": [
        "布尔值",
        "使服务器在服务器列表中看起来是“在线”的。"
    ],
    "enforce-secure-profile": [
        "布尔值",
        "要求玩家必须具有Mojang签名的公钥才能进入服务器。\ntrue - 不具有Mojang签名的公钥的玩家不能进入服务器。\nfalse - 不具有Mojang签名的公钥的玩家也可进入服务器。"
    ],
    "enforce-whitelist": [
        "布尔值",
        "在服务器上强制执行白名单。\n当启用后，不在白名单（前提是启用）中的用户将在服务器重新加载白名单文件后从服务器踢出。\ntrue - 不在白名单上的用户会被踢出。\nfalse - 不在白名单上的在线用户不会被踢出。"
    ],
    "entity-broadcast-range-percentage": [
        "整数（10-1000）",
        "此选项控制实体需要距离玩家有多近才会将数据包发送给客户端。更高的数值意味着实体可以在更远的地方就被渲染，同时也可能提高增加延迟的概率。\n这个值是以默认值的百分比来表示的。例如：将此值设为50，表示将渲染正常情况下一半距离以内的生物。\n此功能模仿了客户端视频设置中的功能，而不像客户端的渲染距离设置一样只能在服务器设置的限制下调整渲染距离。"
    ],
    "force-gamemode": [
        "布尔值",
        "强制玩家加入时为默认游戏模式。\nfalse - 玩家将以退出前的游戏模式加入\ntrue - 玩家总是以默认游戏模式加入"
    ],
    "function-permission-level": [
        "整数（1-4）",
        "设定函数的默认权限等级。"
    ],
    "gamemode": [
        "字符串",
        "定义默认游戏模式。\n如果值是旧用的数字，会静默转换为对应游戏模式的英文名称。\nsurvival (0) - 生存模式\ncreative (1) - 创造模式\nadventure (2) - 冒险模式\nspectator (3) - 旁观模式"
    ],
    "generate-structures": [
        "布尔值",
        "定义是否能生成结构（例如村庄）。\nfalse - 新生成的区块中将不包含结构。\ntrue - 新生成\n的区块中将包含结构。\n注：由于地牢和沙漠水井在技术上属于地物，因而即使此项设为false，其仍然会生成。"
    ],
    "generator-settings": [
        "字符串",
        "本属性质用于自定义世界的生成。"
    ],
    "hardcore": [
        "布尔值",
        "如果设为 true，服务器难度的设置会被忽略并且设为hard（困难），玩家在死后会自动切换至旁观模式。"
    ],
    "hide-online-players": [
        "布尔值",
        "如果设为 true，服务端在响应客户端状态请求时不会返回在线玩家列表。"
    ],
    "initial-disabled-packs": [
        "字符串",
        "需要在创建世界过程中禁用的数据包名称，以逗号分隔。"
    ],
    "initial-enabled-packs": [
        "字符串",
        "需要在创建世界过程中启用的数据包名称，以逗号分隔。特别地，功能数据包必须在此指定才能生效。"
    ],
    "level-name": [
        "字符串",
        "“level-name”的值将作为世界名称及其文件夹名。你也可以把你已生成的世界存档复制过来，然后\n让这个值与那个文件夹的名字保持一致，服务器就可以载入该存档。\n部分字符，例如“'”单引号可能需要在前面加反斜杠号“\\”才能被正常应用。"
    ],
    "level-seed": [
        "字符串",
        "与单人游戏类似，为你的世界定义一个种子。\n这里有一些例子：minecraft，404，1a2b3c。"
    ],
    "level-type": [
        "字符串",
        "使用世界预设ID，确定地图所生成的类型。\n使用世界预设ID时，需要在其中的“:”前加“\\”转义。\n原版世界预设ID可以省略其前面的“minecraft:”（即命名空间）。\nminecraft:normal - 带有丘陵、河谷、海洋等的标准的世界。\nminecraft:flat - 一个没有特性的平坦世界，可用generator-settings修改。\nminecraft:large_biomes - 如同默认的世界，但所有生物群系都更大。\nminecraft:amplified - 如同默认的世界，但世界生成高度提高。\nminecraft:single_biome_surface - 单一生物群系世界，可用generator-settings修改。"
    ],
    "log-ips": [
        "布尔值",
        "是否在有新玩家加入游戏时，在服务器日志中记录其IP地址。\ntrue - 在日志中记录新加入玩家的IP地址。\nfalse - 在日志中隐藏新加入玩家的IP地址。"
    ],
    "max-build-height": [
        "整数",
        "玩家在游戏中能够建造的最大高度。可能会在该值较小时生成超过该值的地形。"
    ],
    "max-chained-neighbor-updates": [
        "整数",
        "限制连锁NC更新的数量，超过此数量的连锁NC更新会被跳过。若为负数则无限制。"
    ],
    "max-players": [
        "整数（0-2147483647）",
        "服务器同时能容纳的最大玩家数量。请注意，在线玩家越多，对服务器造成的负担也就越大。同样注意，服务器的OP具有在人满的情况下强行进入服务器的能力：找到在服务器根目录下叫ops.json的文件并打开，将需要此能力的OP下的bypassesPlayerLimit选项设置为true即可（默认值为false），这意味着OP将不需要在服务器人满时等待有玩家离开后再加入。过大的数值会使客户端显示的玩家列表崩坏。"
    ],
    "max-tick-time": [
        "整数（0–(2^63 - 1)）",
        "设置每个tick花费的最大毫秒数。超过该毫秒数时，服务器watchdog插件将停止服务器程序并附带上信息：服务器的一个tick花费了60.00秒（最长也应该只有0.05秒）；判定服务器已崩溃，它将被强制关闭。遇到这种情况的时候，它会调用 System.exit(1)。\n如果你监测服务程序的返回代码，此时返回代码会为1。（习惯上，程序正常退出应当返回0）\npeaceful-1 - 完全停用watchdog插件（这个停用选项在14w32a快照中添加）"
    ],
    "max-world-size": [
        "整数（1-29999984）",
        "设置可让世界边界获得的最大半径值，单位为方块。通过成功执行的命令能把世界边界设置得更大，但不会超过这里设置的最大方块限制。如果设置的max-world-size超过默认值的大小，那将不会起任何效果。"
    ],
    "motd": [
        "字符串",
        "本属性值是玩家客户端的多人游戏服务器列表中显示的服务器信息，显示于名称下方。\nMOTD 支持样式代码。\nMOTD 支持特殊符号。然而，这些符号需要转换为Unicode转义字符。\n如果MOTD超过59个字符，服务器列表很可能会返回“通讯错误”。"
    ],
    "network-compression-threshold": [
        "整数",
        "默认会允许n-1字节的数据包正常发送, 如果数据包为n字节或更大时会进行压缩。所以，更低的数值会使得更多的数据包被压缩，但是如果被压缩的数据包字节太小将反而使压缩后字节更大。\n-1 - 完全禁用数据包压缩\n0 - 压缩全部数据包\n注：以太网规范要求把小于64字节的数据包填充为64字节。因此，设置一个低于64的值可能没有什么好处。也不推荐让设置的值超过MTU（通常为1500字节）。"
    ],
    "online-mode": [
        "布尔值",
        "是否让服务器对比Minecraft账户数据库验证登录信息。只有在你的服务器并未与Internet连接时，才将这个值设为false。如果设为false，黑客就能够使用任意假账户连接服务器！如果minecraft.net服务器宕机或不可访问，那么该值设为true的服务器会因为无法验证玩家身份而拒绝所有玩家加入。通常，这个值设为true的服务器被称为“正版服务器”。故意设定该变量为false的服务器称为“破解服务器”（也称离线服务器），这类服务器允许拥有未授权的Minecraft副本的玩家加入。\ntrue - 启用。服务器会认为自己具有Internet连接，并检查每一位连入的玩家。\nfalse - 禁用。服务器不会尝试检查玩家。"
    ],
    "op-permission-level": [
        "整数（1-4）",
        "设定使用/op命令时OP的权限等级。所有存档会从之前的存档继承能力和命令。\n1 - OP可以绕过重生点保护。\n2 - OP可以使用所有单人游戏作弊命令（除了/publish，因为不能在服务器上使用；/debug也是）并使用命令方块。命令方块和领域服服主/管理员有此等级权限。\n3 - OP可以使用大多数多人游戏中独有的命令，包括 /debug，以及管理玩家的命令（/ban，/op等等）。\n4 - OP可以使用所有命令，包括 /stop, /save-all, /save-on 和 /save-off。"
    ],
    "player-idle-timeout": [
        "整数",
        "如果不为0，服务器将在玩家的空闲时间达到设置的时间（单位为分钟）时将玩家踢出服务器\n注：当服务器接受到下列数据包之一时将会重置空闲时间：\n点击窗口\n附魔物品\n更新告示牌\n玩家挖掘方块\n玩家放置方块\n更换拿着的物品\n动画（挥动手臂）\n实体动作\n客户端状态\n聊天信息\n使用实体"
    ],
    "prevent-proxy-connections": [
        "布尔值",
        "如果服务器发送的ISP/AS和Mojang的验证服务器的不一样，玩家将会被踢出。\ntrue - 启用。服务器将会禁止玩家使用虚拟专用网络或代理。\nfalse - 禁用。服务器将不会禁止玩家使用虚拟专用网络或代理。"
    ],
    "pvp": [
        "布尔值",
        "是否允许PvP。也只有在允许PvP时玩家自己的箭才会受到伤害。\ntrue - 玩家可以互相伤害。\nfalse - 玩家无法互相造成伤害（也称作玩家对战环境（PvE））。\n注：由玩家造成的间接伤害（例如熔岩，火，TNT等，某种程度上还有水，沙子和沙砾）还是会伤害其他玩家。"
    ],
    "query.port": [
        "整数（1-65534）",
        "设置监听服务器的端口号"
    ],
    "rate-limit": [
        "整数",
        "设置玩家被踢出服务器前，可以发送的数据包数量。\n设置为0表示关闭此功能。"
    ],
    "rcon.password": [
        "字符串",
        "设置RCON远程访问的密码。\nRCON：能允许其他应用程序通过互联网与Minecraft服务器连接并交互的远程控制台协议。"
    ],
    "rcon.port": [
        "整数（1-65534)",
        "设置RCON远程访问的端口号。"
    ],
    "require-resource-pack": [
        "布尔值",
        "当此选项启用（设为true）时，玩家会被提示作出选择（是否启用服务器资源包）。如果玩家拒绝则会被服务器断开连接。\n但是，若玩家使用Linux系统加入服务器，游戏目录内的server-resource-packs没有写权限，则会提示“无法应用服务器资源包”“所有依赖自定义资源包的功能都有可能不按预期工作”，并提示玩家“继续”或“断开连接”。若玩家选择“继续”，则仍可在此服务器中游戏。"
    ],
    "resource-pack": [
        "字符串",
        "可选选项，可输入指向一个资源包的URI。玩家可选择是否使用该资源包。\n注意若该值含冒号和等号字符，需要在其前加上反斜线(\\)，例如 http\\://somedomain.com/somepack.zip?someparam\\=somevalue 资源包大小理应不能超过\n50 MiB（1.15-pre5前）\n100 MiB（1.15-pre5到1.18-pre8）\n250 MiB（1.18-rc1起）\n注意，下载成功或失败由客户端记录，而非服务器。"
    ],
    "resource-pack-prompt": [
        "字符串",
        "可选，用于在使用require-resource-pack时在资源包提示界面显示自定义信息。\n与聊天组件语法一致，可以包含多行文本。"
    ],
    "resource-pack-sha1": [
        "字符串",
        "资源包的SHA-1值，必须为小写十六进制，建议填写它。这还没有用于验证资源包的完整性，但是它提高了资源包缓存的有效性和可靠性。"
    ],
    "server-ip": [
        "字符串",
        "将服务器与一个特定IP绑定。强烈建议留空该属性值！\n留空，或是填入你想让服务器绑定（监听）的IP。"
    ],
    "server-port": [
        "整数（1-65534）",
        "改变服务器（监听的）端口号。如果服务器在使用NAT的网络中运行，该端口必须被转发（在你有家用路由器/防火墙的前提下）。"
    ],
    "simulation-distance": [
        "整数（3-32）",
        "设置服务端可更新实体范围的最大值，即玩家各个方向上的区块数量（是以玩家为中心的半径，不是直径）。超出此范围的实体不会被更新，对玩家也不可见。\n默认/推荐设置为10，如果有严重卡顿的话，减少该数值。"
    ],
    "spawn-animals": [
        "布尔值",
        "决定动物是否可以生成。\ntrue - 动物可以正常生成。\nfalse - 动物生成后会立即消失。\n提示：如果你有严重的卡顿，可以设为false。"
    ],
    "spawn-monsters": [
        "布尔值",
        "决定攻击型生物（怪物）是否可以生成。\ntrue - 启用。怪物会生成于夜晚和黑暗处。\nfalse - 禁用。不会有任何怪物。\n如果difficulty=0（即难度设置为和平）的话，该属性值不会有任何影响。\n提示：如果你有严重的卡顿，可以设为false。"
    ],
    "spawn-npcs": [
        "布尔值",
        "决定是否生成村民。\ntrue - 启用。生成村民。\nfalse - 禁用。不生成村民。"
    ],
    "spawn-protection": [
        "整数",
        "通过将该值进行2x+1的运算来决定出生点的保护半径。设置为1会保护以出生点为中心的3×3方块的区域，2会保护5×5方块的区域，3会保护7×7方块的区域，以此类推。这个选项不在第一次服务器启动时生成，只会在第一个玩家加入服务器时出现。如果服务器没有设置OP，这个选项会自动禁用。\n设置为0将不会禁用出生点保护，但会保护位于出生点的那一个方块（13w05a前）。\n设置为0会禁用出生点保护（13w05a起）。"
    ],
    "sync-chunk-writes": [
        "布尔值",
        "启用后区块文件以同步模式写入。"
    ],
    "text-filtering-config": [
        "字符串",
        "服务器中需要被屏蔽的文本。"
    ],
    "use-native-transport": [
        "布尔值",
        "是否使用针对Linux平台的数据包收发优化。此选项仅会在Linux平台上生成。\ntrue - 启用。启用Linux数据包收发优化。\nfalse - 禁用。禁用Linux数据包收发优化。"
    ],
    "view-distance": [
        "整数（3-32）",
        "设置服务端发送给客户端的世界数据量，也就是设置玩家各个方向上的区块数量（是以玩家为中心的半径，不是直径）。它决定了服务端的可视距离。（另见渲染距离）\n默认/推荐设置为10，如果有严重卡顿的话，减少该数值。"
    ],
    "white-list": [
        "布尔值",
        "启用服务器的白名单。\n当启用时，只有白名单上的用户才能连接服务器。白名单主要用于私人服务器，例如提供给相识的朋友、通过应用流程谨慎选择的陌生人等。\nfalse - 不使用白名单。\ntrue - 从whitelist.json文件加载白名单。\n注: OP会自动被视为在白名单上，所以无需再将OP加入白名单。"
    ],
    "announce-player-achievements": [
        "布尔值",
        "(仅Java版1.12前版本)用于切换是否成就要广播给所有玩家。"
    ],
    "snooper-enabled": [
        "布尔值",
        "是否允许服务端定期发送统计数据到Mojang官方。"
    ]
}"""
from multiprocessing import cpu_count

ui = {
    "Java": {
        "enable-jmx-monitoring": {
            "type": "bool",
            "tip": "暴露一个具有对象名net.minecraft.server:type=Server的MBean和两个属性averageTickTime和tickTimes用于暴露以毫秒为单位的tick时间。"
        },
        "rcon.port": {
            "type": "int",
            "range": [1, 65535],
            "step": 1,
            "tip": "设置RCON远程访问的端口号。"
        },
        "level-seed": {
            "type": "str",
            "tip": "设置世界的种子。"
        },
        "gamemode": {
            "type": "enum",
            "values": ["survival", "creative", "adventure", "spectator"],
            "tip": "定义默认游戏模式。\n如果值是旧用的数字，会静默转换为对应游戏模式的英文名称。\nsurvival (0) - 生存模式\ncreative (1) - 创造模式\nadventure (2) - 冒险模式\nspectator (3) - 旁观模式"
        },
        "enable-command-block": {
            "type": "bool",
            "tip": "是否启用命令方块。"
        },
        "enable-query": {
            "type": "bool",
            "tip": "允许使用GameSpy4协议的服务器监听器。用于获取服务器信息。"
        },
        "generator-settings": {
            "type": "str",
            "tip": "本属性质用于自定义世界的生成。"
        },
        "enforce-secure-profile": {
            "type": "bool",
            "tip": "要求玩家必须具有Mojang签名的公钥才能进入服务器。\ntrue - 不具有Mojang签名的公钥的玩家不能进入服务器。\nfalse - 不具有Mojang签名的公钥的玩家也可进入服务器。"
        },
        "level-name": {
            "type": "str",
            "tip": "“level-name”的值将作为世界名称及其文件夹名。你也可以把你已生成的世界存档复制过来，然后\n让这个值与那个文件夹的名字保持一致，服务器就可以载入该存档。\n部分字符，例如“'”单引号可能需要在前面加反斜杠号“\\”才能被正常应用。"
        },
        "motd": {
            "type": "str",
            "tip": "本属性值是玩家客户端的多人游戏服务器列表中显示的服务器信息，显示于名称下方。\nMOTD 支持样式代码。\nMOTD 支持特殊符号。然而，这些符号需要转换为Unicode转义字符。\n如果MOTD超过59个字符，服务器列表很可能会返回“通讯错误”。"
        },
        "query.port": {
            "type": "int",
            "range": [1, 65535],
            "step": 1,
            "tip": "设置监听服务器的端口号"
        },
        "pvp": {
            "type": "bool",
            "tip": "是否允许玩家互相攻击。"
        },
        "generate-structures": {
            "type": "bool",
            "tip": "定义是否能生成结构（例如村庄）。\nfalse - 新生成的区块中将不包含结构。\ntrue - 新生成\n的区块中将包含结构。\n注：由于地牢和沙漠水井在技术上属于地物，因而即使此项设为false，其仍然会生成。"
        },
        "max-chained-neighbor-updates": {
            "type": "int",
            "tip": "限制连锁NC更新的数量，超过此数量的连锁NC更新会被跳过。若为负数则无限制。"
        },
        "difficulty": {
            "type": "enum",
            "values": ["peaceful", "easy", "normal", "hard"],
            "tip": "定义服务器的游戏难度。\n如果设置了旧的数字ID，则会自动转化为英文的难度名称。\npeaceful (0) - 和平\neasy (1) - 简单\nnormal (2) - 普通\nhard (3) - 困难"
        },
        "network-compression-threshold": {
            "type": "ext-enum",
            "values": [-1, 0],
            "ext-type": "int",
            "ext-range": [64, 1500],
            "tip": "默认会允许n-1字节的数据包正常发送, 如果数据包为n字节或更大时会进行压缩。所以，更低的数值会使得更多的数据包被压缩，但是如果被压缩的数据包字节太小将反而使压缩后字节更大。\n-1 - 完全禁用数据包压缩\n0 - 压缩全部数据包\n注：以太网规范要求把小于64字节的数据包填充为64字节。因此，设置一个低于64的值可能没有什么好处。也不推荐让设置的值超过MTU（通常为1500字节）。"
        },
        "max-tick-time": {
            "type": "int",
            "tip": "设置每个tick花费的最大毫秒数。超过该毫秒数时，服务器watchdog插件将停止服务器程序并附带上信息：服务器的一个tick花费了60.00秒（最长也应该只有0.05秒）；判定服务器已崩溃，它将被强制关闭。遇到这种情况的时候，它会调用 System.exit(1)。\n如果你监测服务程序的返回代码，此时返回代码会为1。（习惯上，程序正常退出应当返回0）\npeaceful-1 - 完全停用watchdog插件（这个停用选项在14w32a快照中添加）"
        },
        "require-resource-pack": {
            "type": "bool",
            "tip": "当此选项启用（设为true）时，玩家会被提示作出选择（是否启用服务器资源包）。如果玩家拒绝则会被服务器断开连接。\n但是，若玩家使用Linux系统加入服务器，游戏目录内的server-resource-packs没有写权限，则会提示“无法应用服务器资源包”“所有依赖自定义资源包的功能都有可能不按预期工作”，并提示玩家“继续”或“断开连接”。若玩家选择“继续”，则仍可在此服务器中游戏。"

        },
        "use-native-transport": {
            "type": "bool",
            "tip": "是否使用针对Linux平台的数据包收发优化。此选项仅会在Linux平台上生成。\ntrue - 启用。启用Linux数据包收发优化。\nfalse - 禁用。禁用Linux数据包收发优化。"
        },
        "max-players": {
            "type": "int",  # 太大或者无法确定时，type=int时，不需要指定range和step
            "tip": "服务器同时能容纳的最大玩家数量。请注意，在线玩家越多，对服务器造成的负担也就越大。同样注意，服务器的OP具有在人满的情况下强行进入服务器的能力：找到在服务器根目录下叫ops.json的文件并打开，将需要此能力的OP下的bypassesPlayerLimit选项设置为true即可（默认值为false），这意味着OP将不需要在服务器人满时等待有玩家离开后再加入。过大的数值会使客户端显示的玩家列表崩坏。"
        },
        "online-mode": {
            "type": "bool",
            "tip": "是否让服务器对比Minecraft账户数据库验证登录信息。只有在你的服务器并未与Internet连接时，才将这个值设为false。如果设为false，黑客就能够使用任意假账户连接服务器！如果minecraft.net服务器宕机或不可访问，那么该值设为true的服务器会因为无法验证玩家身份而拒绝所有玩家加入。通常，这个值设为true的服务器被称为“正版服务器”。故意设定该变量为false的服务器称为“破解服务器”（也称离线服务器），这类服务器允许拥有未授权的Minecraft副本的玩家加入。\ntrue - 启用。服务器会认为自己具有Internet连接，并检查每一位连入的玩家。\nfalse - 禁用。服务器不会尝试检查玩家。"
        },
        "enable-status": {
            "type": "bool",
            "tip": "使服务器在服务器列表中看起来是“在线”的。"
        },
        "allow-flight": {
            "type": "bool",
            "tip": "允许玩家在安装添加飞行功能的mod前提下在生存模式下飞行。\n允许飞行可能会使恶意破坏者更加常见，因为此设定会使他们更容易达成目的。在创造模式下无作用。\nfalse - 不允许飞行。悬空超过5秒的玩家会被踢出服务器。\ntrue - 允许飞行。玩家得以使用任何能飞行的mod飞行。"
        },
        "broadcast-rcon-to-ops": {
            "type": "bool",
            "tip": "向所有在线OP发送通过RCON执行的命令的输出。"
        },
        "view-distance": {
            "type": "int",
            "range": [3, 32],
            "step": 1,
            "tip": "设置服务端发送给客户端的世界数据量，也就是设置玩家各个方向上的区块数量（是以玩家为中心的半径，不是直径）。它决定了服务端的可视距离。（另见渲染距离）\n默认/推荐设置为10，如果有严重卡顿的话，减少该数值。"
        },
        "server-ip": {
            "type": "str",
            "tip": "将服务器与一个特定IP绑定。强烈建议留空该属性值！\n留空，或是填入你想让服务器绑定（监听）的IP。"
        },
        "resource-pack-prompt": {
            "type": "str",
            "tip": "可选，用于在使用require-resource-pack时在资源包提示界面显示自定义信息。\n与聊天组件语法一致，可以包含多行文本。"
        },
        "allow-nether": {
            "type": "bool",
            "tip": "允许玩家进入下界。\nfalse - 下界传送门不会生效。\ntrue - 玩家可以通过下界传送门前往下界。"
        },
        "server-port": {
            "type": "int",
            "range": [1, 65535],
            "step": 1,
            "tip": "改变服务器（监听的）端口号。如果服务器在使用NAT的网络中运行，该端口必须被转发（在你有家用路由器/防火墙的前提下）。"
        },
        "enable-rcon": {
            "type": "bool",
            "tip": "是否允许远程访问服务器控制台。\n由于RCON协议传输数据时没有加密，所以不建议把RCON暴露在互联网上。RCON客户端和服务端交换的所有数据（包括RCON密码）都会泄露给正在监听此连接的人。"
        },
        "sync-chunk-writes": {
            "type": "bool",
            "tip": "启用后区块文件以同步模式写入。"
        },
        "op-permission-level": {
            "type": "int",
            "range": [1, 4],
            "step": 1,
            "tip": "设定使用/op命令时OP的权限等级。所有存档会从之前的存档继承能力和命令。\n1 - OP可以绕过重生点保护。\n2 - OP可以使用所有单人游戏作弊命令（除了/publish，因为不能在服务器上使用；/debug也是）并使用命令方块。命令方块和领域服服主/管理员有此等级权限。\n3 - OP可以使用大多数多人游戏中独有的命令，包括 /debug，以及管理玩家的命令（/ban，/op等等）。\n4 - OP可以使用所有命令，包括 /stop, /save-all, /save-on 和 /save-off。"
        },
        "prevent-proxy-connections": {
            "type": "bool",
            "tip": "如果服务器发送的ISP/AS和Mojang的验证服务器的不一样，玩家将会被踢出。\ntrue - 启用。服务器将会禁止玩家使用虚拟专用网络或代理。\nfalse - 禁用。服务器将不会禁止玩家使用虚拟专用网络或代理。"
        },
        "hide-online-players": {
            "type": "bool",
            "tip": "如果设为 true，服务端在响应客户端状态请求时不会返回在线玩家列表。"
        },
        "resource-pack": {
            "type": "str",
            "tip": "当此选项启用（设为true）时，玩家会被提示作出选择（是否启用服务器资源包）。如果玩家拒绝则会被服务器断开连接。\n但是，若玩家使用Linux系统加入服务器，游戏目录内的server-resource-packs没有写权限，则会提示“无法应用服务器资源包”“所有依赖自定义资源包的功能都有可能不按预期工作”，并提示玩家“继续”或“断开连接”。若玩家选择“继续”，则仍可在此服务器中游戏。"
        },
        "entity-broadcast-range-percentage": {
            "type": "int",
            "range": [10, 1000],
            "tip": "此选项控制实体需要距离玩家有多近才会将数据包发送给客户端。更高的数值意味着实体可以在更远的地方就被渲染，同时也可能提高增加延迟的概率。\n这个值是以默认值的百分比来表示的。例如：将此值设为50，表示将渲染正常情况下一半距离以内的生物。\n此功能模仿了客户端视频设置中的功能，而不像客户端的渲染距离设置一样只能在服务器设置的限制下调整渲染距离。"

        },
        "simulation-distance": {
            "type": "int",
            "range": [3, 32],
            "step": 1,
            "tip": "设置服务端可更新实体范围的最大值，即玩家各个方向上的区块数量（是以玩家为中心的半径，不是直径）。超出此范围的实体不会被更新，对玩家也不可见。\n默认/推荐设置为10，如果有严重卡顿的话，减少该数值。"
        },
        "rcon.password": {
            "type": "str",
            "tip": "设置RCON远程访问的密码。\nRCON：能允许其他应用程序通过互联网与Minecraft服务器连接并交互的远程控制台协议。"
        },
        "player-idle-timeout": {
            "type": "int",
            "tip": "如果不为0，服务器将在玩家的空闲时间达到设置的时间（单位为分钟）时将玩家踢出服务器\n注：当服务器接受到下列数据包之一时将会重置空闲时间：\n点击窗口\n附魔物品\n更新告示牌\n玩家挖掘方块\n玩家放置方块\n更换拿着的物品\n动画（挥动手臂）\n实体动作\n客户端状态\n聊天信息\n使用实体"

        },
        "force-gamemode": {
            "type": "bool",
            "tip": "强制玩家加入时为默认游戏模式。\nfalse - 玩家将以退出前的游戏模式加入\ntrue - 玩家总是以默认游戏模式加入"
        },
        "rate-limit": {
            "type": "int",
            "tip": "设置玩家被踢出服务器前，可以发送的数据包数量。\n设置为0表示关闭此功能。"
        },
        "hardcore": {
            "type": "bool",
            "tip": "如果设为 true，服务器难度的设置会被忽略并且设为hard（困难），玩家在死后会自动切换至旁观模式。"
        },
        "white-list": {
            "type": "bool",
            "tip": "启用服务器的白名单。\n当启用时，只有白名单上的用户才能连接服务器。白名单主要用于私人服务器，例如提供给相识的朋友、通过应用流程谨慎选择的陌生人等。\nfalse - 不使用白名单。\ntrue - 从whitelist.json文件加载白名单。\n注: OP会自动被视为在白名单上，所以无需再将OP加入白名单。"

        },
        "broadcast-console-to-ops": {
            "type": "bool",
            "tip": "向所有在线OP发送所执行命令的输出。"
        },
        "spawn-npcs": {
            "type": "bool",
            "tip": "决定是否生成村民。\ntrue - 启用。生成村民。\nfalse - 禁用。不生成村民。"
        },
        "spawn-animals": {
            "type": "bool",
            "tip": "决定是否生成动物。\ntrue - 启用。生成动物。\nfalse - 禁用。不生成动物。"
        },
        "log-ips": {
            "type": "bool",
            "tip": "是否在有新玩家加入游戏时，在服务器日志中记录其IP地址。\ntrue - 在日志中记录新加入玩家的IP地址。\nfalse - 在日志中隐藏新加入玩家的IP地址。"
        },
        "function-permission-level": {
            "type": "int",
            "range": [1, 4],
            "step": 1,
            "tip": "设定函数的默认权限等级。"
        },
        "initial-enabled-packs": {
            "type": "str",
            "tip": "需要在创建世界过程中启用的数据包名称，以逗号分隔。特别地，功能数据包必须在此指定才能生效。"
        },
        "level-type": {
            "type": "ext-enum",
            "values": ["normal", "flat", "largeBiomes", "amplified", "single_biome_surface"],
            "ext-type": "str",
            "tip": "使用世界预设ID，确定地图所生成的类型。\n使用世界预设ID时，需要在其中的“:”前加“\\”转义。\n原版世界预设ID可以省略其前面的“minecraft:”（即命名空间）。\nminecraft:normal - 带有丘陵、河谷、海洋等的标准的世界。\nminecraft:flat - 一个没有特性的平坦世界，可用generator-settings修改。\nminecraft:large_biomes - 如同默认的世界，但所有生物群系都更大。\nminecraft:amplified - 如同默认的世界，但世界生成高度提高。\nminecraft:single_biome_surface - 单一生物群系世界，可用generator-settings修改。"

        },
        "text-filtering-config": {
            "type": "str",
            "tip": "服务器中需要被屏蔽的文本。"
        },
        "spawn-monsters": {
            "type": "bool",
            "tip": "决定攻击型生物（怪物）是否可以生成。\ntrue - 启用。怪物会生成于夜晚和黑暗处。\nfalse - 禁用。不会有任何怪物。\n如果difficulty=0（即难度设置为和平）的话，该属性值不会有任何影响。\n提示：如果你有严重的卡顿，可以设为false。"
        },
        "enforce-whitelist": {
            "type": "bool",
            "tip": "在服务器上强制执行白名单。\n当启用后，不在白名单（前提是启用）中的用户将在服务器重新加载白名单文件后从服务器踢出。\ntrue - 不在白名单上的用户会被踢出。\nfalse - 不在白名单上的在线用户不会被踢出。"
        },
        "spawn-protection": {
            "type": "int",
            "tip": "通过将该值进行2x+1的运算来决定出生点的保护半径。设置为1会保护以出生点为中心的3×3方块的区域，2会保护5×5方块的区域，3会保护7×7方块的区域，以此类推。这个选项不在第一次服务器启动时生成，只会在第一个玩家加入服务器时出现。如果服务器没有设置OP，这个选项会自动禁用。\n设置为0将不会禁用出生点保护，但会保护位于出生点的那一个方块（13w05a前）。\n设置为0会禁用出生点保护（13w05a起）。"

        },
        "resource-pack-sha1": {
            "type": "str",
            "tip": "资源包的SHA-1值，必须为小写十六进制，建议填写它。这还没有用于验证资源包的完整性，但是它提高了资源包缓存的有效性和可靠性。"
        },
        "max-world-size": {
            "type": "int",
            "tip": "设置可让世界边界获得的最大半径值，单位为方块。通过成功执行的命令能把世界边界设置得更大，但不会超过这里设置的最大方块限制。如果设置的max-world-size超过默认值的大小，那将不会起任何效果。"
        }
    },
    "Bedrock": {
        "server-name": {
            "type": "str",
        },
        "server-port": {
            "type": "int",
            "range": [1, 65535],
            "step": 1,
        },
        "server-portv6": {
            "type": "int",
            "range": [1, 65535],
            "step": 1,
        },
        "max-players": {
            "type": "int",
        },
        "level-name": {
            "type": "str",
        },
        "level-seed": {
            "type": "str",
        },
        "default-player-permission-level": {
            "type": "int",
            "range": [0, 4],
            "step": 1,
        },
        "texturepack-required": {
            "type": "bool",
        },
        "content-log-file-enabled": {
            "type": "bool",
        },
        "compression-threshold": {
            "type": "int",
            "range": [0, 65535],
            "step": 1,
        },
        "server-authoritative-movement": {
            "type": "bool",
        },
        "player-idle-timeout": {
            "type": "int",
        },
        "view-distance": {
            "type": "int",
            "range": [3, 64],
            "step": 1,
        },
        "tick-distance": {
            "type": "int",
            "range": [4, 12],
            "step": 1,
        },
        "player-movement-score-threshold": {
            "type": "int",
        },
        "player-movement-distance-threshold": {
            "type": "num",
        },
        "player-movement-duration-threshold-in-ms": {
            "type": "int",
        },
        "correct-player-movement": {
            "type": "bool",
        },
        "server-authoritative-block-breaking": {
            "type": "bool",
        },
        "movement-score-threshold": {
            "type": "int",
        },
        "movement-distance-threshold": {
            "type": "num",
        },
        "movement-duration-threshold-in-ms": {
            "type": "int",
        },
        "allow-cheats": {
            "type": "bool",
        },
        "max-threads": {
            "type": "int",
            "range": [1, cpu_count()],
            "step": 1,
        },
        "level-type": {
            "type": "enum",
            "values": ["DEFAULT", "FLAT", "LEGACY"],
        }
    }
}