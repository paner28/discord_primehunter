from discord.ext import commands
import discord
import os
import sympy

TOKEN = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()

class data:
    jflag = False
    kmax = 10**15
    kmin = 0

@client.event
async def on_ready():
    bot_channel = client.get_channel(701367378386223114)
    await bot_channel.send("server start!")
    print("server start!")

@client.event
async def on_message(message):
    global channel,pl
    channel = client.get_channel(685797761290993681)
    pl = []
    if message.channel.name == "素数判定":
        if message.author.bot:
            return
        if data.jflag:
            kn = message.content
            if int(kn) != 0:
                data.kmax = 10**(int(kn))
                data.kmin = 10**(int(kn)-1)
            elif int(kn) == 0:
                data.kmax = 10**15
                data.kmin = 0
        else:
            global num,t
            k = []
            num = [-3] * 100
            msg = message.content
            k = list(msg)
            t = len(k)
            print(k)

        if data.jflag:
            await fx(t)
            await make_list(pl)
            data.jflag = False
            data.kmax = 10**15
            data.kmin = 0
            return

        await change(k)
        print(nk)

        if "x" in msg:
            data.jflag = True
            await channel.send("桁数を入力してください")

        else:
            await judge(nk,t)
    else:
        return

async def judge(nk,t):
    p = 0
    for i in range(t):
        if nk[i] < 10:
            p *= 10
        else:
            p *= 100
        p += nk[i]
    if sympy.isprime(int(p)):
        await channel.send(str(p) + "は素数です")
    else:
        await channel.send(str(p) + "=" + str(sympy.factorint(int(p))))
    return

async def change(k):
    global nk
    nk = []
    k = ["10" if i == "t" or i == "T" else i for i in k]
    k = ["11" if i == "j" or i == "J" else i for i in k]
    k = ["12" if i == "q" or i == "Q" else i for i in k]
    k = ["13" if i == "k" or i == "K" else i for i in k]
    k = ["14" if i == "x" or i == "X" else i for i in k]
    try:
        k = [int(i) for i in k]
    except:
        await channel.send("半角自然数を入力してください")
    nk = k
    return nk

async def fx(n):
    for i in range(n):
        if nk[i] == 14:
            nk[i] = -1
            for j in range(1,14):
                num[i] = j
                await fx(n)
            nk[i] = 14
            return
        elif nk[i] == -1:
            continue
        else:
            num[i] = nk[i]
    q = 0
    for i in range(n):
        if num[i] < 10:
            q *= 10
        else:
            q *= 100
        q += num[i]
    if q > data.kmin and q < data.kmax and sympy.isprime(q) == True:
        pl.append(q)
    
async def make_list(pl):
    pc = len(pl)
    mflag = [0] * 100000
    maisuu = [[0] * 13 for i in range(100000)]
    print(pl)
    for i in range(pc):
        for j in range(i+1,pc):
            if pl[i]>pl[j]:
                pl[i],pl[j] = pl[j],pl[i]
        for j in range(13):
            if maisuu[i][j] > 4:
                mflag[i] = 1
    for i in range(pc-2,1,-1):
        if mflag[i] == 0:
            for j in range(i+1,pc):
                if maisuu[i] == maisuu[j]:
                    mflag[i] = 1

    for i in range(len(pl)):
        await channel.send(str(pl[i]) + "は素数です")

client.run(TOKEN)
