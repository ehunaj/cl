# -*- coding: utf-8 -*-

from linepy import *
from akad.ttypes import Message
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator

botStart = time.time()

cl = LINE()
cl.log("Auth Token : " + str(cl.authToken))
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

clMID = cl.profile.mid
clProfile = cl.getProfile()
clSettings = cl.getSettings()
oepoll = OEPoll(cl)
call = cl
read = json.load(readOpen)
settings = json.load(settingsOpen)

Bots = [clMID]
admin = "ub3808de9f7df35f57fb366d157f9790a"
bl = {
     "blacklist":{}
}
wait = {
    "Bot": True,
    "mention":"║┝──────────────\n║│Yuk kak chat sini 🙋\n║╰❉ Jangan ngelamun😁\n╰━━━━━━━━━━━━━━━━n  ━━━━┅═❉ই۝ई❉═┅━━━━",
    "Respontag":"Hoi Jgn ngtag semm",
    "welcome":"Selamat datang & semoga betah",
    "comment":"Like like & like by Ehun",
    "message":"Terimakasih sudah add saya"
    }
settings = {
    "autoAdd": False,
    "autoJoin": False,
    "autoJoinTicket":True,
    "autoLeave": False,
    "autoRead": False,
    "lang":"JP",
    "detectMention": True,
    "detectMentionadmin": True,
    "changeGroupPicture":[],
    "notifikasi": False,
    "Sider":{},
    "checkSticker": False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

cctv = {
    "cyduk":{},
    "point":{},
    "MENTION":{},
    "sidermem":{}
}

myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus

def restartBot():
    print ("[ INFO ] BOT RESETTED")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Haii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))


def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, Message, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "╭━━━┅═❉ই۝ई❉═┅━━━━\n║ Haii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    pass
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def backupData():
    try:
        backup = bl
        f = codecs.open('bl.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def helpmessage():
    helpMessage = "━━━━┅═❉ই۝ई❉═┅━━━━\n          ❇    SELFBOT    ❇\n╭━━━━━━━━━━━━━━━━\n║╭❉ MENU HELP ❇\n║┝───────────────" + "\n" + \
                  "║┝──[❇ STATUS ❇ ]" + "\n" + \
                  "║│ Restart" + "\n" + \
                  "║│ Runtime" + "\n" + \
                  "║│ Speed" + "\n" + \
                  "║│ Status" + "\n" + \
                  "║│ Bot(on/off" + "\n" + \
                  "║│ Dell「Removechat」" + "\n" + \
                  "║┝───────────────" + "\n" + \
                  "║┝──[ ❇ SETTING ❇ ]" + "\n" + \
                  "║│ Allstatus「On/Off」" + "\n" + \
                  "║│ Notif「On/Off」" + "\n" + \
                  "║│ Sider「On/Off」" + "\n" + \
                  "║│ AutoAdd「On/Off」" + "\n" + \
                  "║│ AutoJoin「On/Off」" + "\n" + \
                  "║│ AutoLeave「On/Off」" + "\n" + \
                  "║│ AutoRead「On/Off」" + "\n" + \
                  "║│ CheckSticker「On/Off」" + "\n" + \
                  "║│ DetectMention「On/Off」" + "\n" + \
                  "║┝───────────────" + "\n" + \
                  "║┝──[ ❇  SELF  ❇]" + "\n" + \
                  "║│ Me" + "\n" + \
                  "║│ MyMid" + "\n" + \
                  "║│ MyName" + "\n" + \
                  "║│ MyBio" + "\n" + \
                  "║│ MyPicture" + "\n" + \
                  "║│ MyVideoProfile" + "\n" + \
                  "║│ MyCover" + "\n" + \
                  "║│ StealContact「@」" + "\n" + \
                  "║│ StealMid「@」" + "\n" + \
                  "║│ StealName「@」" + "\n" + \
                  "║│ StealBio「@」" + "\n" + \
                  "║│ StealPicture「@」" + "\n" + \
                  "║│ StealVideoProfile「@」" + "\n" + \
                  "║│ StealCover「@」" + "\n" + \
                  "║│ CloneProfile「@」" + "\n" + \
                  "║│ RestoreProfile" + "\n" + \
                  "║┝───────────────" + "\n" + \
                  "║┝──[ ❇ GROUP ❇ ]" + "\n" + \
                  "║│ GroupCreator" + "\n" + \
                  "║│ GroupId" + "\n" + \
                  "║│ GroupName" + "\n" + \
                  "║│ GroupPicture" + "\n" + \
                  "║│ GroupTicket" + "\n" + \
                  "║│ GroupTicket「On/Off」" + "\n" + \
                  "║│ GroupList" + "\n" + \
                  "║│ GroupMemberList" + "\n" + \
                  "║│ GroupInfo" + "\n" + \
                  "║│ Mimic「On/Off」" + "\n" + \
                  "║│ MimicList" + "\n" + \
                  "║│ MimicAdd「@」" + "\n" + \
                  "║│ MimicDel「@」" + "\n" + \
                  "║│ Tag" + "\n" + \
                  "║│ Lurking「On/Off/Reset」" + "\n" + \
                  "║│ Lurking" + "\n" + \
                  "║┝───────────────" + "\n" + \
                  "║┝──[ ❇ MEDIA ❇]" + "\n" + \
                  "║│ Kalender" + "\n" + \
                  "║│ CheckDate「Date」" + "\n" + \
                  "║┝───────────────\n║╰❉      EHUN BOT      ❇\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━"
    return helpMessage

def clBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] END OF OPERATION")
            return
        if op.type == 5:
            print ("[ 5 ] NOTIFIED ADD CONTACT")
            if settings["autoAdd"] == True:
                cl.sendMessage(op.param1, "Halo {} terimakasih telah menambahkan saya sebagai teman :D".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 13:
            print ("[ 13 ] NOTIFIED INVITE GROUP")
            group = cl.getGroup(op.param1)
            if settings["autoJoin"] == True:
                cl.acceptGroupInvitation(op.param1)
                cl.inviteIntoGroup(op.param1,admin)

        if op.type == 17:
            if op.param2 in bl["blacklist"]:
               cl.cancelGroupInvitaion(op.param1,[op.param2])
               cl.kickoutFromGroup(op.param1,[op.param2])
               bl["blacklist"][op.param2] = True

        if op.type == 19:
            if op.param3 in admin:
                if op.param2 in clMID:
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    bl["blacklist"][op.param2] = True

        if op.type == 24:
            print ("[ 24 ] NOTIFIED LEAVE ROOM")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                cl.sendText(msg.to,"Bot Sudah On Kembali")

        if op.type == 25 or op.type == 26:
          if wait["Bot"] == True:
            print ("[ 25 ] SEND MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif text.lower() == 'bot on':
                  if msg._from in admin:
                      wait["Bot"] == True
                      cl.sendMessage(to,"Ok actip")
                elif text.lower() == 'bot off':
                  if msg._from in admin:
                      wait["Bot"] == False
                      cl.sendMessage(to,"Ok Non actip")
                elif 'Sampah' in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(to,[_mid])
                elif text.lower() == "cek":
                  if msg._from in admin:
                    if wait["Bot"] == True:
                        try:cl.inviteIntoGroup(to, [clMID]);has = "OK"
                        except:has = "NOT"
                        try:cl.kickoutFromGroup(to, [clMID]);has1 = "OK"
                        except:has1 = "NOT"
                        if has == "OK":sil = "🔋██ full 100%"
                        else:sil = "🔌█▒. Low 0%"
                        if has1 == "OK":sil1 = "🔋██ full 100%"
                        else:sil1 = "🔌█▒ Low 0%"
                        cl.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                elif "Leave" in msg.text:
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      gid = cl.getGroupIdsJoined()
                      for i in gid:
                          cl.sendMessage(i,"Bot Di Paksa Keluar Oleh Owner!\nAyo left teman2\nAssalamualikum wr wb All Member|nAdd Owner kami")
                          cl.sendContact(i,"ub3808de9f7df35f57fb366d157f9790a")
                          cl.leaveGroup(i)
                elif ("Undang " in msg.text):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      targets = []
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          if target not in admin:
                              try:
                                  cl.inviteIntoGroup(to,target)
                              except:
                                  pass

                elif ("Kick " in msg.text):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      targets = []
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          if target not in admin:
                              try:
                                  bl["blacklist"][target] = True
                                  cl.kickoutFromGroup(to,[target])
                              except:
                                  pass
                elif text.lower() == 'banlist':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if bl["blacklist"] == {}:
                          cl.sendMessage(to,"Tidak Ada")
                      else:
                          mcs = ""
                          for mi_d in bl["blacklist"]:
                               mcs += "->" +cl.getContact(mi_d).displayName + "\n"
                          cl.sendMessage(to,"===[Blacklist User]===\n"+ mcs)
                elif text.lower() == 'clear':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                        bl["blacklist"] = {}
                        cl.sendMessage(to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All")
                elif text.lower() == 'dell':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      cl.removeAllMessages(op.param2)
                      cl.sendMessage(to, "Menghapus Chat")
                elif text.lower() == 'speed':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      start = time.time()
                      elapsed_time = time.time() - start
                      cl.sendMessage(to,format(str(elapsed_time)))
                elif text.lower() == 'restart':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      cl.sendMessage(to, "Sudah di restart...")
                      restartBot()
                elif text.lower() == 'runtime':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      timeNow = time.time()
                      runtime = timeNow - botStart
                      runtime = format_timespan(runtime)
                      cl.sendMessage(to, "Bot Aktif Selama {}".format(str(runtime)))
                elif text.lower() == 'status':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      try:
                          ret_ = "━━━━┅═❉ই۝ई❉═┅━━━━\n          ❇    STATUS    ❇\n╭━━━━━━━━━━━━━━━━\n║╭❉ 🔵[ON]|[OFF]🔴 ❇\n║┝───────────────"
                          if settings["autoAdd"] == True: ret_ += "\n║│🔵 Auto Add [ON]"
                          else: ret_ += "\n║│🔴 Auto Add [OFF]"
                          if settings["autoJoin"] == True: ret_ += "\n║│🔵 Auto Join [ON]"
                          else: ret_ += "\n║│🔴 Auto Join [OFF]"
                          if settings["autoLeave"] == True: ret_ += "\n║│🔵 Auto Leave [ON]"
                          else: ret_ += "\n║│🔴 Auto Leave [OFF]"
                          if settings["autoRead"] == True: ret_ += "\n║│🔵 Auto Read [ON]"
                          else: ret_ += "\n║│🔴 Auto Read [OFF]"
                          if settings["notifikasi"] == True: ret_ += "\n║│🔵 Notif [ON]"
                          else: ret_ += "\n║│🔴 Notif [OFF]"
                          if settings["detectMention"] == True: ret_ += "\n║│🔵 Detect Mention [ON]"
                          else: ret_ += "\n║│🔴 Detect Mention [OFF]"
                          ret_ += "\n║┝───────────────\n║╰❉      EHUN  BOT      ❇\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━"
                          cl.sendMessage(to, str(ret_))
                      except Exception as e:
                          cl.sendMessage(to, str(e))
                elif text.lower() == 'autoadd on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoAdd"] = True
                      cl.sendMessage(to, "mengaktifkan Auto Add")
                elif text.lower() == 'autoadd off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoAdd"] = False
                      cl.sendMessage(to, "menonaktifkan Auto Add")
                elif text.lower() == 'autojoin on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoJoin"] = True
                      cl.sendMessage(to, "mengaktifkan Auto Join")
                elif text.lower() == 'autojoin off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoJoin"] = False
                      cl.sendMessage(to, "menonaktifkan Auto Join")
                elif text.lower() == 'autoleave on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoLeave"] = True
                      cl.sendMessage(to, "mengaktifkan Auto Leave")
                elif text.lower() == 'autojoin off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoLeave"] = False
                      cl.sendMessage(to, "menonaktifkan Auto Leave")
                elif text.lower() == 'autoread on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoRead"] = True
                      cl.sendMessage(to, "mengaktifkan Auto Read")
                elif text.lower() == 'autoread off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["autoRead"] = False
                      cl.sendMessage(to, "menonaktifkan Auto Read")
                elif text.lower() == 'checksticker on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["checkSticker"] = True
                      cl.sendMessage(to, "mengaktifkan Check Details Sticker")
                elif text.lower() == 'checksticker off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["checkSticker"] = False
                      cl.sendMessage(to, "menonaktifkan Check Details Sticker")
                elif text.lower() == 'detectmention on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["datectMention"] = True
                      cl.sendMessage(to, "mengaktifkan Detect Mention")
                elif text.lower() == 'detectmention off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["datectMention"] = False
                      cl.sendMessage(to, "menonaktifkan Detect Mention")

                elif text.lower() == 'allstatus on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["notifikasi"] = True
                      settings["autoAdd"] = True
                      settings["autoJoin"] = True
                      settings["autoLeave"] = True
                      settings["autoRead"] = True
                      settings["datectMention"] = True
                      cl.sendMessage(to, "Allstatus bot mode on")

                elif text.lower() == 'allstatus off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      settings["notifikasi"] = False
                      settings["autoAdd"] = False
                      settings["autoJoin"] = False
                      settings["autoLeave"] = False
                      settings["autoRead"] = False
                      settings["datectMention"] = False
                      cl.sendMessage(to, "Allstatus bot mode on")

                elif text.lower() == 'me':
                      sendMessageWithMention(to, msg._from) #clMID)
                      cl.sendContact(to, msg._from) #clMID)
                elif text.lower() == 'mymid':
                      cl.sendMessage(to,"[MID]\n" +  clMID)
                elif text.lower() == 'myname':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      me = cl.getContact(clMID)
                      cl.sendMessage(to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == 'mybio':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      me = cl.getContact(clMID)
                      cl.sendMessage(to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == 'mypicture':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      me = cl.getContact(clMID)
                      cl.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == 'myvideoprofile':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      me = cl.getContact(clMID)
                      cl.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == 'mycover':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      me = cl.getContact(clMID)
                      cover = cl.getProfileCoverURL(clMID)    
                      cl.sendImageWithURL(to, cover)
                elif msg.text.lower().startswith("stealcontact "):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(to, mi_d)
                elif msg.text.lower().startswith("stealmid "):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        cl.sendMessage(to, str(ret_))
                elif msg.text.lower().startswith("stealname "):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith("stealbio "):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("stealpicture "):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(to, str(path))
                elif msg.text.lower().startswith("stealvideoprofile "):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.cl.naver.jp/" + cl.getContact(ls).pictureStatus + "/vp"
                            cl.sendImageWithURL(to, str(path))
                elif msg.text.lower().startswith("stealcover "):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if cl != None:
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(to, str(path))
                elif msg.text.lower().startswith("cloneprofile "):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            cl.cloneContactProfile(contact)
                            cl.sendMessage(to, "clone member ")
                        except:
                            cl.sendMessage(to, "Gagal clone member")
                elif text.lower() == 'restoreprofile':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      try:
                          clProfile.displayName = str(myProfile["displayName"])
                          clProfile.statusMessage = str(myProfile["statusMessage"])
                          clProfile.pictureStatus = str(myProfile["pictureStatus"])
                          cl.updateProfileAttribute(8, clProfile.pictureStatus)
                          cl.updateProfile(clProfile)
                          cl.sendMessage(to, "restore profile ")
                      except:
                          cl.sendMessage(to, "Gagal restore profile")

                elif msg.text.lower().startswith("mimicadd "):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              settings["mimic"]["target"][target] = True
                              cl.sendMessage(to,"Target ditambahkan!")
                              break
                          except:
                              cl.sendMessage(to,"Added Target Fail !")
                              break
                elif msg.text.lower().startswith("mimicdel "):
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      targets = []
                      key = eval(msg.contentMetadata["MENTION"])
                      key["MENTIONEES"][0]["M"]
                      for x in key["MENTIONEES"]:
                          targets.append(x["M"])
                      for target in targets:
                          try:
                              del settings["mimic"]["target"][target]
                              cl.sendMessage(to,"Target dihapuskan!")
                              break
                          except:
                              cl.sendMessage(to,"Deleted Target Fail !")
                              break
                elif text.lower() == 'mimiclist':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if settings["mimic"]["target"] == {}:
                          cl.sendMessage(msg.to,"Tidak Ada Target")
                      else:
                          mc = "╔══[ Mimic List ]"
                          for mi_d in settings["mimic"]["target"]:
                              mc += "\n╠ "+cl.getContact(mi_d).displayName
                          cl.sendMessage(to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      sep = text.split(" ")
                      mic = text.replace(sep[0] + " ","")
                      if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            cl.sendMessage(msg.to,"Reply Message on")
                      elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            cl.sendMessage(to,"Reply Message off")

                elif text.lower() == 'groupcreator':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      group = cl.getGroup(to)
                      GS = group.creator.mid
                      cl.sendContact(to, GS)
                elif text.lower() == 'groupid':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      gid = cl.getGroup(to)
                      cl.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == 'grouppicture':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      group = cl.getGroup(to)
                      path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                      cl.sendImageWithURL(to, path)
                elif text.lower() == 'groupname':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      gid = cl.getGroup(to)
                      cl.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                elif text.lower() == 'groupticket':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ Group Ticket ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "Grup qr tidak terbuka silahkan buka terlebih dahulu dengan perintah {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == 'groupticket on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "Grup qr sudah terbuka")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "membuka grup qr")
                elif text.lower() == 'groupticket off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "Grup qr sudah tertutup")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "menutup grup qr")
                elif text.lower() == 'groupinfo':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      group = cl.getGroup(to)
                      try:
                          gCreator = group.creator.displayName
                      except:
                          gCreator = "Tidak ditemukan"
                      if group.invitee is None:
                          gPending = "0"
                      else:
                          gPending = str(len(group.invitee))
                      if group.preventedJoinByTicket == True:
                          gQr = "Tertutup"
                          gTicket = "Tidak ada"
                      else:
                          gQr = "Terbuka"
                          gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                      path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                      ret_ = "╔══[ Group Info ]"
                      ret_ += "\n╠ Nama Group : {}".format(str(group.name))
                      ret_ += "\n╠ ID Group : {}".format(group.id)
                      ret_ += "\n╠ Pembuat : {}".format(str(gCreator))
                      ret_ += "\n╠ Jumlah Member : {}".format(str(len(group.members)))
                      ret_ += "\n╠ Jumlah Pending : {}".format(gPending)
                      ret_ += "\n╠ Group Qr : {}".format(gQr)
                      ret_ += "\n╠ Group Ticket : {}".format(gTicket)
                      ret_ += "\n╚══[ Group Info ]"
                      cl.sendMessage(to, str(ret_))
                      cl.sendImageWithURL(to, path)
                elif text.lower() == 'groupmemberlist':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'grouplist':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                        groups = cl.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'notif on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if settings["notifikasi"] == True:
                        if settings["lang"] == "JP":
                            cl.sendMessage(to,"notif mode on")
                        else:
                            settings["notifikasi"] = True
                            if settings["lang"] == "JP":
                                cl.sendMessage(to,"notif mode on")

                elif text.lower() == 'notif off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if settings["notifikasi"] == False:
                        if settings["lang"] == "JP":
                          cl.sendMessage(to,"notif mode off")
                      else:
                          settings["notifikasi"] = False
                          if settings["lang"] == "JP":
                              cl.sendMessage(to,"notif mode off")
                elif text.lower() == 'tag':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 0:
                          sendMention(to, to, "", "")
                      elif msg.toType == 2:
                            group = cl.getGroup(to)
                            midMembers = [contact.mid for contact in group.members]
                            midSelect = len(midMembers)//20
                            for mentionMembers in range(midSelect+1):
                                no = 0
                                ret_ = "╔══[ Mention Members ]"
                                dataMid = []
                                for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                    dataMid.append(dataMention.mid)
                                    no += 1
                                    ret_ += "\n╠ {}. @!".format(str(no))
                                ret_ += "\n╚══[ Total {} Members]".format(str(len(dataMid)))
                                cl.sendMention(to, ret_, dataMid)
                elif text.lower() == 'changepictureprofile':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                        settings["changePicture"] = True
                        cl.sendMessage(to, "Silahkan kirim gambarnya")
                elif text.lower() == 'changegrouppicture':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.toType == 2:
                        if to not in settings["changeGroupPicture"]:
                            settings["changeGroupPicture"].append(to)
                            cl.sendMessage(to, "Silahkan kirim gambarnya")
                elif text.lower() == 'lurking on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      tz = pytz.timezone("Asia/Jakarta")
                      timeNow = datetime.now(tz=tz)
                      day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                      hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                      bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                      hr = timeNow.strftime("%A")
                      bln = timeNow.strftime("%m")
                      for i in range(len(day)):
                          if hr == day[i]: hasil = hari[i]
                      for k in range(0, len(bulan)):
                          if bln == str(k): bln = bulan[k-1]
                      readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                      if msg.to in read['readPoint']:
                          try:
                              del read['readPoint'][msg.to]
                              del read['readMember'][msg.to]
                              del read['readTime'][msg.to]
                          except:
                              pass
                          read['readPoint'][msg.to] = msg.id
                          read['readMember'][msg.to] = ""
                          read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                          read['ROM'][msg.to] = {}
                          with open('read.json', 'w') as fp:
                              json.dump(read, fp, sort_keys=True, indent=4)
                              cl.sendMessage(to,"Lurking already on")
                      else:
                          try:
                              del read['readPoint'][msg.to]
                              del read['readMember'][msg.to]
                              del read['readTime'][msg.to]
                          except:
                              pass
                          read['readPoint'][msg.to] = msg.id
                          read['readMember'][msg.to] = ""
                          read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                          read['ROM'][msg.to] = {}
                          with open('read.json', 'w') as fp:
                              json.dump(read, fp, sort_keys=True, indent=4)
                              cl.sendMessage(to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'lurking off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      tz = pytz.timezone("Asia/Jakarta")
                      timeNow = datetime.now(tz=tz)
                      day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                      hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                      bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                      hr = timeNow.strftime("%A")
                      bln = timeNow.strftime("%m")
                      for i in range(len(day)):
                          if hr == day[i]: hasil = hari[i]
                      for k in range(0, len(bulan)):
                          if bln == str(k): bln = bulan[k-1]
                      readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                      if msg.to not in read['readPoint']:
                          cl.sendMessage(to,"Lurking already off")
                      else:
                          try:
                              del read['readPoint'][msg.to]
                              del read['readMember'][msg.to]
                              del read['readTime'][msg.to]
                          except:
                              pass
                          cl.sendMessage(to, "Delete reading point:\n" + readTime)

                elif text.lower() == 'lurking reset':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      tz = pytz.timezone("Asia/Jakarta")
                      timeNow = datetime.now(tz=tz)
                      day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                      hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                      bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                      hr = timeNow.strftime("%A")
                      bln = timeNow.strftime("%m")
                      for i in range(len(day)):
                          if hr == day[i]: hasil = hari[i]
                      for k in range(0, len(bulan)):
                          if bln == str(k): bln = bulan[k-1]
                      readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                      if msg.to in read["readPoint"]:
                          try:
                              del read["readPoint"][msg.to]
                              del read["readMember"][msg.to]
                              del read["readTime"][msg.to]
                          except:
                              pass
                          cl.sendMessage(to, "Reset reading point:\n" + readTime)
                      else:
                          cl.sendMessage(to, "Lurking belum diaktifkan ngapain di reset?")

                elif text.lower() == 'lurking':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      tz = pytz.timezone("Asia/Jakarta")
                      timeNow = datetime.now(tz=tz)
                      day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                      hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                      bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                      hr = timeNow.strftime("%A")
                      bln = timeNow.strftime("%m")
                      for i in range(len(day)):
                          if hr == day[i]: hasil = hari[i]
                      for k in range(0, len(bulan)):
                          if bln == str(k): bln = bulan[k-1]
                      readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                      if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            cl.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = cl.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        cl.sendMessage(receiver,"Lurking has not been set.")

                elif text.lower() == 'sider on':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      try:
                          del cctv['point'][msg.to]
                          del cctv['sidermem'][msg.to]
                          del cctv['cyduk'][msg.to]
                      except:
                          pass
                      cctv['point'][msg.to] = msg.id
                      cctv['sidermem'][msg.to] = ""
                      cctv['cyduk'][msg.to]=True 
                      settings["Sider"] = True
                      cl.sendMessage(to,"SIDER SUDAH ON")

                elif text.lower() == 'sider off':
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      if msg.to in cctv['point']:
                          cctv['cyduk'][msg.to]=False
                          settings["Sider"] = False
                          cl.sendMessage(to,"SIDER SUDAH OFF")
                      else:
                          cl.sendMessage(to,"SIDER SUDAH OFF")

                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    cl.sendMessage(to, readTime)                 
                elif "checkdate" in msg.text.lower():
                  if msg._from in admin:
                    if wait["Bot"] == True:
                      sep = msg.text.split(" ")
                      tanggal = msg.text.replace(sep[0] + " ","")
                      r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                      data=r.text
                      data=json.loads(data)
                      ret_ = ""
                      ret_ += "Date Of Birth : {}".format(str(data["data"]["lahir"]))
                      ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                      ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                      ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                      ret_ += ""
                      cl.sendMessage(to, str(ret_))
                elif "/ti/g/" in msg.text.lower():
                      if settings["autoJoinTicket"] == True:
                          link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                          links = link_re.findall(text)
                          n_links = []
                          for l in links:
                              if l not in n_links:
                                  n_links.append(l)
                          for ticket_id in n_links:
                              group = cl.findGroupByTicket(ticket_id)
                              cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                              cl.sendMessage(to, "Masuk : %s" % str(group.name))

            elif msg.contentType == 7:
                if settings["checkSticker"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    ret_ = ""
                    ret_ += "STICKER ID : {}".format(stk_id)
                    ret_ += "\nSTICKER PACKAGES ID : {}".format(pkg_id)
                    ret_ += "\nSTICKER VERSION : {}".format(stk_ver)
                    ret_ += "\nSTICKER URL : line://shop/detail/{}".format(pkg_id)
                    ret_ += ""
                    cl.sendMessage(to, str(ret_))

            elif msg.contentType == 1:
                    if settings["changePicture"] == True:
                        path = cl.downloadObjectMsg(msg_id)
                        settings["changePicture"] = False
                        cl.updateProfilePicture(path)
                        cl.sendMessage(to, "mengubah foto profile")
                    if msg.toType == 2:
                        if to in settings["changeGroupPicture"]:
                            path = cl.downloadObjectMsg(msg_id)
                            settings["changeGroupPicture"].remove(to)
                            cl.updateGroupPicture(to, path)
                            cl.sendMessage(to, "mengubah foto group")

        if op.type == 26:
            print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                              if settings["detectMention"] == True:
                                 sendMention(receiver, sender, "", " \nWoy Jgn ngetag semm kak ?? ")

                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if admin in mention["M"]:
                              if settings["detectMentionadmin"] == True:
                                 sendMention(receiver, sender, "", " \nJangan ngetag Creator ku kak\nDia gi sibuk!!!!!!")

#"╭━━━━┅═❉ই۝ई❉═┅━━━\n║╭Woy kak","", "\n║│Kesepian ya  🙋\n║╰❉ Jangan ngetag semm😁\n╰━━━━━━━━━━━━━━━━")

#"", " \nWoy kamu kesepian yak?? ")

        if op.type == 17:
           print ("MEMBER JOIN TO GROUP")
           if settings["notifikasi"] == True:
             if op.param2 in clMID:
                 return
             ginfo = cl.getGroup(op.param1)
             contact = cl.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             cl.sendMessage(op.param1,"Halo... " + cl.getContact(op.param2).displayName + "\nSelamat datang di\n💎 " + str(ginfo.name) + " 💎" + "\n jangan lupa ngenot \n& Semoga betah ya😃")
             cl.sendImageWithURL(op.param1,image)

        if op.type == 15:
           print ("MEMBER LEAVE TO GROUP")
           if settings["notifikasi"] == True:
             if op.param2 in clMID:
                 return
             ginfo = cl.getGroup(op.param1)
             contact = cl.getContact(op.param2)
             image = "http://dl.profile.line.naver.jp/" + contact.pictureStatus
             cl.sendImageWithURL(op.param1,image)
             cl.sendMessage(op.param1,"Naah nahh.... " + cl.getContact(op.param2).displayName + "\nBaper tingkat tinggi😂")

        #if op.type == 55:
            #print ("[ 55 ] NOTIFIED READ MESSAGE")
            #try:
                #if cctv['cyduk'][op.param1]==True:
                    #if op.param1 in cctv['point']:
                        #Name = cl.getContact(op.param2).displayName
                        #if Name in cctv['sidermem'][op.param1]:
                            #pass
                        #else:
                            #cctv['sidermem'][op.param1] += "\nâ¢ " + Name
                            #if " " in Name:
                                #nick = Name.split(' ')
                                #if len(nick) == 2:
                                    #cl.sendMessage(op.param1, "╭━━━━┅═❉ই۝ई❉═┅━━━━\n║╭❉ SIDER TERDETEKSI\n║┝───────────────\n" + "║│" + nick[0] + "\n║┝─────────────── " + "\n║│Yuk kak chat sini 🙋\n║╰❉ Jangan ngelamun😁\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━ ")
                                    #time.sleep(0.2)
                                    #siderMembers(op.param1, [op.param2]) #mentionMembers(op.param1,[op.param2])
                                #else:
                                    #cl.sendMessage(op.param1, "╭━━━━┅═❉ই۝ई❉═┅━━━━\n║╭❉ SIDER TERDETEKSI\n║┝───────────────\n" + "║│" + nick[0] + "\n║┝─────────────── " + "\n║│Yuk kak chat sini 🙋\n║╰❉ Jangan ngelamun😁\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━ ")
                                    #time.sleep(0.2)
                                    #siderMembers(op.param1, [op.param2]) #mentionMembers(op.param1,[op.param2])
                            #else:
                                #cl.sendMessage(op.param1, "╭━━━━┅═❉ই۝ई❉═┅━━━━\n║╭❉ SIDER TERDETEKSI\n║┝───────────────\n" + "║│" + Name + "\n║┝─────────────── " + "\n║│Yuk kak chat sini 🙋\n║╰❉ Jangan ngelamun😁\n╰━━━━━━━━━━━━━━━━\n━━━━┅═❉ই۝ई❉═┅━━━━ ")
                                #time.sleep(0.2)
                                #siderMembers(op.param1, [op.param2]) #mentionMembers(op.param1,[op.param2])
                    #else:
                        #pass
                #else:
                    #pass
            #except:
                #pass
        if op.type == 55:
            print ("Sider")
            try:
                if cctv['cyduk'][op.param1]==True:
                    if op.param1 in cctv['point']:
                        Name = cl.getContact(op.param2).displayName
                        if Name in cctv['sidermem'][op.param1]:
                            pass
                        else:
                            cctv['sidermem'][op.param1] += "\n~ " + Name
                            siderMembers(op.param1, [op.param2])
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(op.param1, image)
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                clBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
