# -*- coding: utf-8 -*
from linepy import *
from akad.ttypes import Message
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator

import time, asyncio, json, threading, codecs, sys, os, re, urllib, requests,subprocess,traceback,random
from Naked.toolshed.shell import execute_js 
from bs4 import BeautifulSoup

creator = ["u9d79f5031bc4c73a5054aa8b26c9d0c2"]

helpMessage ="""
_.key_
_.add owner_
_.del owner_
_.add admin_
_.del admin_
_.add staff_
_.del staff_
_.cban_
_.autojoin on:off_
_.add on:off_
_.kick @_
_.sp_
_.runtime_
_.bye_
_.rechat_
"""

with open('pro.json', 'r') as fp:
    pro = json.load(fp)
with open('org.json', 'r') as fp:
    org = json.load(fp)
with open('wait2.json', 'r') as fp:
    wait2 = json.load(fp)

mulai = time.time()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","?","???:","???:","????","????"]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

class LineBot(object):
    
    def __init__(self, resp, authQR=None):
        self.resp = resp
        self.resp = self.resp+' '
        self.authQR = authQR
        self.login(authQR)
        self.fetch()

    def AutoSave(self,op):
        msg = op.message
        self.client.unsend2(msg,self.wait)
        self.client.fancyfancy(self.wait)
        with open(self.anus, 'w') as fp:
            json.dump(self.wait, fp, sort_keys=True, indent=4, ensure_ascii=False)
        
    def login(self, auth):
        if auth == None:
            self.client = LINE()
        else:
            self.client = LINE(auth)
        self.client.log("Auth Token : " + str(self.client.authToken))
        self.mid = self.client.getProfile().mid

    def fetch(self):
        while True:
            try:
                self.operations = self.client.poll.fetchOperations(self.client.revision, 50)
                for op in self.operations:
                    if (op.type != OpType.END_OF_OPERATION):
                        self.client.revision = max(self.client.revision, op.revision)
                        self.bot(op)
                        self.AutoSave(op)
            except:
                pass
        
    def bot(self, op):
        cl = self.client
        wait = wait2
        try:
            if op.type == 0 or op.type == 50:
                return

            if op.type == 13:
                if self.mid in op.param3:
                    if wait2["autoJoin"] == True:
                        if op.param2 not in creator and op.param2 not in org["owner"]:
                            cl.acceptGroupInvitation(op.param1)
                            ginfo = cl.getGroup(op.param1)
                            cl.sendMessage(op.param1,"hi mem " + str(ginfo.name))
                            cl.sendMessage(op.param1,"Bukan Owner ia... Balik lagi ah??\nn Bye..")
                            cl.leaveGroup(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            cl.getGrpup(op.param1)
                            if op.param3 in org["owner"] and op.param3 in creator and op.param3 in org["admin"] and op.param3 in org["staff"]:
                                if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                                    wait2["blacklist"][op.param2] = True
                                    with open('wait2.json','w',) as fp:
                                        json.dump(wait2, fp, sort_keys=True, indent=4)
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    cl.cancelGroupInvitation(op.param1,[op.param2])

                if self.mid in op.param3:
                    if op.param2 in org["owner"] or op.param2 in org["staff"]:
                        cl.acceptGroupInvitation(op.param1)

            if op.type == 13:
                if op.param2 in wait2["blacklist"]:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param3])
                    except:
                        pass

                if op.param1 in pro["Proinvite"]:
                    if op.param2 in creator or op.param2 in org["owner"] or op.param2 in org["admin"] or op.param2 in org["staff"]:
                        pass
                    else:
                        wait2["blacklist"][op.param2] = True
                        with open('wait2.json','w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        group = cl.getContact(op.param3)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                          if _mid in op.param3:
                            cl.cancelGroupInvitation(op.param1,[_mid])

            if op.type == 13:
                if op.param3 in wait2["blacklist"]:
                    if op.param2 in creator or op.param2 in org["owner"] or op.param2 in org["admin"] or op.param2 in org["staff"]:
                        pass
                    else:
                        wait2["blacklist"][op.param2] = True
                        with open('wait2.json','w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param3])

            if op.type == 19:
                if op.param1 in pro["Autokick"]:
                    if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        wait2["blacklist"][op.param2] = True
                        with open('wait2.json','w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        if op.param3 not in wait2["blacklist"]:
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])

                if op.param3 in creator:
                    if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        wait2["blacklist"][op.param2] = True
                        with open('wait2.json','w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.acceptGroupInvitation(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])

                if op.param3 in org["owner"]:
                    if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        wait2["blacklist"][op.param2] = True
                        with open('wait2.json','w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.acceptGroupInvitation(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])

                if op.param3 in org["admin"]:
                    if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        wait2["blacklist"][op.param2] = True
                        with open('wait2.json','w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])

                if op.param3 in org["staff"]:
                    if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        wait2["blacklist"][op.param2] = True
                        with open('wait2.json','w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])

            if op.type == 0:
                return

            if op.type == 5:
                cl.findAndAddContactsByMid(op.param1)
                if(wait2["message"]in[""," ","\n",None]):
                    pass
                else:
                    cl.sendMessage(op.param1,str(wait2["message"]))

            if op.type == 15:
                if op.param1 in wait2["bymsg"]:
                    if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        return
                    else:
                        cl.sendText(op.param1, wait2["leftmsg"])
                        print ("MEMBER HAS LEFT THE GROUP")

            if op.type == 17:
                if op.param2 in wait2["blacklist"]:
                    if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        cl.kickoutFromGroup(op.param1,[op.param2])

            if op.type == 32:
                if op.param1 in pro["Procancel"]:
                    if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        wait2["blacklist"][op.param2] = True
                        with open('wait2.json','w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        if op.param3 not in wait2["blacklist"]:
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])

                if wait2["Jscancel"] == True:
                    if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        wait2["blacklist"][op.param2] = True
                        with open('wait2.json','w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        user = cl.getContact(op.param2)
                        cl.sendMessage(op.param2,"jangan di cancel woooii.. " + str(user.displayName))
                        try:
                            if op.param3 in org["owner"]:
                                cl.findAndAddContactsByMid(op.param3)
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 in creator:
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass

            if op.type == 11:
                if op.param1 in pro["Proqr"]:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                            wait2["blacklist"][op.param2] = True
                            with open('wait2.json','w') as fp:
                                json.dump(wait2, fp, sort_keys=True, indent=4)
                            cl.reissueGroupTicket(op.param1)
                            G = cl.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.kickoutFromGroup(op.param1,[op.param2])

                if op.param2 in wait2["blacklist"]:
                    if op.param2 not in creator and op.param2 not in org["owner"] and op.param2 not in org["admin"] and op.param2 not in org["staff"]:
                        if cl.getGroup(op.param1).preventedJoinByTicket == False:
                            cl.reissueGroupTicket(op.param1)
                            G = cl.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.kickoutFromGroup(op.param1,[op.param2])

            if op.type == 11:
                if op.param1 in pro["Proname"]:
                    if op.param2 in creator or op.param2 in org["owner"] or op.param2 in org["admin"] or op.param2 in org["staff"]:
                        pass
                    else:
                        g = cl.getGroup(op.param1)
                        g.name = pro["gname"][op.param1]
                        cl.updateGroup(g)

            if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 and msg.toType == 2:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                else:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                if msg.contentType == 13:
                  if msg._from in creator:
                    if wait2["addowner"] == True:
                        if msg.contentMetadata["mid"] in org["owner"]:
                            cl.sendMessage(msg.to, "was owner")
                        else:
                            org["owner"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to, "owner added")

                if msg.contentType == 13:
                  if msg._from in creator:
                    if wait2["delowner"] == True:
                        if msg.contentMetadata["mid"] in org["owner"]:
                            del org["owner"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to,"Owner deleted")
                        else:
                            cl.sendMessage(msg.to,"Owner not found")
#===[ Add admin ☆☆☆ ]
                if msg.contentType == 13:
                  if msg._from in creator or msg._from in org["owner"]:
                    if wait2["addadmin"]==True:
                        if msg.contentMetadata["mid"] in org["admin"]:
                            cl.sendMessage(msg.to, "was admin")
                            wait2["addadmin"]=False
                        else:
                            org["admin"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to, "admin added")
                            wait2["addadmin"]=False

                if msg.contentType == 13:
                  if msg._from in creator or msg._from in org["owner"]:
                    if wait2["deladmin"]==True:
                        if msg.contentMetadata["mid"] in org["admin"]:
                            del org["admin"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            wait2["deladmin"]=False
                            cl.sendMessage(msg.to,"s deleted")
                        else:
                            cl.sendMessage(msg.to,"S not found")
#====[ Add staff ☆☆☆ ]
                if msg.contentType == 13:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if wait2["addstaff"]==True:
                        if msg.contentMetadata["mid"] in org["staff"]:
                            cl.sendMessage(msg.to, "was staff")
                            wait2["addstaff"]=False
                        else:
                            org["staff"][msg.contentMetadata["mid"]] = True
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to, "staff added")
                            wait2["addstaff"]=False

                if msg.contentType == 13:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if wait2["delstaff"]==True:
                        if msg.contentMetadata["mid"] in org["staff"]:
                            del org["staff"][msg.contentMetadata["mid"]]
                            with open('org.json', 'w') as fp:
                                json.dump(org, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to,"staff deleted")
                            wait2["delstaff"]=False
                        else:
                            cl.sendMessage(msg.to,"Staff not found")
                            wait2["delstaff"]=False
#========[ BLACKLIST ]============#
                if msg.contentType == 13:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if wait2["ablacklist"]==True:
                        if msg.contentMetadata["mid"] in wait2["blacklist"]:
                            cl.sendMessage(to, "Was BL boss")
                            wait2["ablacklist"]=False
                        else:
                            wait2["blacklist"][msg.contentMetadata["mid"]] = True
                            with open('wait2.json', 'w') as fp:
                                json.dump(wait2, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "Blacklist Saved")
                            wait2["ablacklist"]=False

                if msg.contentType == 13:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if wait2["dblacklist"]==True:
                        if msg.contentMetadata["mid"] in wait2["blacklist"]:
                            del wait2["blacklist"][msg.contentMetadata["mid"]]
                            with open('wait2.json', 'w') as fp:
                                json.dump(wait2, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "Blacklist Removed")
                            wait2["dblacklist"]=False
                        else:
                            cl.sendMessage(to," target not found")
                            wait2["dblacklist"]=False
                if msg.contentType == 13:
                  if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                    if wait2["Invi"] == True:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = cl.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                cl.sendMessage(msg.to,"-> " + _name + " was here")
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(msg.to,[target])
                                cl.sendMessage(msg.to,"Done Invite : " + _name)

            if op.type == 26:
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 and msg.toType == 2:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                else:
                    to = receiver
                if msg.contentType == 7:
                    pass
                elif text is None:
                    return
                elif msg.toType == 2:
                    if msg.text == self.resp + "help":
                      if msg._from in creator:
                        cl.sendMessage(msg.to,helpMessage)
                    if msg.text in [".key owner"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        cl.sendMessage(msg.to,helpMessage1)
                    if msg.text in [".key admin"]:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        cl.sendMessage(msg.to,helpMessage2)
                    elif msg.text in [".reboot"]:
                        if msg._from in creator:
                            print ("[Command]Like executed")
                            try:
                                cl.sendMessage(msg.to,"Restarting...")
                                restart_program()
                            except:
                                cl.sendMessage(msg.to,"Please wait")
                                restart_program()
                                pass
                    elif msg.text in [".absen"]:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                          cl.sendMessage(msg.to, "stay...")
                    elif msg.text == self.resp + "key":
                      if msg._from in creator or msg._from in org["owner"]:
                          md = "        _[]   ??     []_\n\n"
                          md += "" +self.resp+ " key\n"
                          md += "" +self.resp+ " owner\n"
                          md += "" +self.resp+ " admin\n"
                          md += "" +self.resp+ " staff\n"
                          md += "" +self.resp+ " banlist\n"
                          md += "" +self.resp+ " kick\n"
                          md += "" +self.resp+ " cancel\n"
                          md += "" +self.resp+ " ourl\n"
                          md += "" +self.resp+ " curl\n"
                          md += "" +self.resp+ " grupset\n"
                          md += "" +self.resp+ " grup\n"
                          md += "" +self.resp+ " invite\n"
                          md += "" +self.resp+ " inv to\n"
                          md += "" +self.resp+ " bye\n"
                          md += "" +self.resp+ " left in\n"
                          md += "" +self.resp+ " ct\n"
                          md += "" +self.resp+ " mid\n\n"
                          md += " _[] ?? []_"
                          cl.sendMessage(msg.to,md)
                    elif self.resp + "ct @" in msg.text:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
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
                                cl.sendContact(msg.to, mi_d)
                    elif self.resp + "cn " in msg.text:
                      if msg._from in creator:
                        x = cl.getProfile()
                        x.displayName = msg.text.replace("cn ","")
                        cl.updateProfile(x)
                        cl.sendMessage(msg.to, " done")
                    elif msg.text in [".runtime"]:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        eltime = time.time() - mulai
                        van = "Bot run "+waktu(eltime)
                        cl.sendMessage(msg.to,van)
                    elif msg.text == self.resp + "ourl":
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        X = cl.getGroup(msg.to)
                        if X.preventedJoinByTicket == False:
                            cl.updateGroup(X)
                            gurl = cl.reissueGroupTicket(msg.to)
                            cl.sendMessage(msg.to,"line://ti/g/" + gurl)
                        else:
                            X.preventedJoinByTicket = False
                            cl.updateGroup(X)
                            gurl = cl.reissueGroupTicket(msg.to)
                            cl.sendMessage(msg.to,"line://ti/g/" + gurl)
                    elif msg.text == self.resp + "curl":
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        X = cl.getGroup(msg.to)
                        if X.preventedJoinByTicket == True:
                            cl.sendMessage(msg.to,"qr was close")
                        else:
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.sendMessage(msg.to,"done..")
                    elif self.resp + "mid @" in msg.text:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        if 'MENTION' in msg.contentMetadata.keys() != None:
                            names = re.findall(r'@(\w+)', msg.text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            for mention in mentionees:
                                try:
                                    cl.sendMessage(msg.to,str(mention['M']))
                                except Exception as e:
                                    pass
                    elif ".kick " in msg.text:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target in org["admin"] or target in org["staff"]:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass

                    elif msg.text == self.resp + "nodeall":
                      if msg._from in creator:
                            cmd = 'kickall.js gid={} token={}'.format(receiver, cl.authToken)
                            group = cl.getGroup(receiver)
                            members = [o.mid for o in group.members if o.mid not in creator and o.mid not in org["owner"] and o.mid not in org["admin"] and o.mid not in org["staff"]]
                            for invitees in group.invitee:
                              for o in group.members:
                                if invitees.mid not in org["owner"]:
                                  if o.mid not in org["owner"]:
                                    cmd += ' uid={}'.format(invitees.mid)
                                    cmd += ' uid={}'.format(o.mid)
                            print(cmd)
                            success = execute_js(cmd)

                    elif msg.text == self.resp + "nodes":
                      if msg._from in creator:
                        cmd = 'nook.js gid={} token={}'.format(to, cl.authToken)
                        group = cl.getGroup(to)
                        for a in creator:
                            cl.sendMessage(a, "im has been used js from group %s" %group.name)
                            members = [o.mid for o in group.members if o.mid not in creator and o.mid not in org["owner"] and o.mid not in org["admin"] and o.mid not in org["staff"]]
                            for o in group.members:
                              if o.mid not in creator and o.mid not in org["staff"]:
                                cmd += ' uid={}'.format(o.mid)
                            print(cmd)
                            success = execute_js(cmd)

                    elif self.resp + "kick " in msg.text:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        for target in targets:
                            if target in org["admin"] or target in org["staff"]:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                except:
                                    pass
                    elif msg.text in [".bot cancel"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        group = cl.getGroup(msg.to)
                        if group.invitee is None:
                            cl.sendMessage(op.message.to, " gada pendingan bos..")
                        else:
                            nama = [contact.mid for contact in group.invitee]
                            for x in nama:
                              if x not in org["owner"]:
                                cl.cancelGroupInvitation(msg.to, [x])
                                time.sleep(0.3)
                            cl.sendMessage(msg.to, "done.")

                    elif msg.text == self.resp + "cancel":
                      if msg._from in creator or msg._from in org["owner"]:
                        group = cl.getGroup(msg.to)
                        if group.invitee is None:
                            cl.sendMessage(op.message.to, "gada pendingan bos..")
                        else:
                            nama = [contact.mid for contact in group.invitee]
                            for x in nama:
                              if x not in org["owner"]:
                                cl.cancelGroupInvitation(msg.to, [x])
                                time.sleep(0.3)
                            cl.sendMessage(to, "done.")
                    elif msg.text == self.resp + "grup":
                        if msg._from in creator:
                            gid = cl.getGroupIdsJoined()
                            h = ""
                            for i in gid:
                                gn = cl.getGroup(i).name
                                h += " %s\n" % (gn)
                            cl.sendMessage(msg.to,"My grup \n"+ h)
                    elif self.resp + "inv to " in msg.text:
                      if msg._from in creator:
                        ng = msg.text.replace("inv to ","")
                        gid = cl.getGroupIdsJoined()
                        x = msg._from
                        for i in gid:
                                h = cl.getGroup(i).name
                                if h == ng:
                                    cl.inviteIntoGroup(i,[x])
                                    cl.sendMessage(msg.to,"Success join to ["+ h +"] group")
                                else:
                                    pass
                    elif self.resp + "leave grup " in msg.text:
                      if msg._from in creator:
                        ng = msg.text.replace("leave grup ","")
                        gid = cl.getGroupIdsJoined()
                        for i in gid:
                            h = cl.getGroup(i).name
                            if h == ng:
                                cl.sendMessage(i,"Bot di paksa keluar oleh owner!")
                                cl.leaveGroup(i)
                                cl.sendMessage(msg.to,"Success left ["+ h +"] group")
                            else:
                                pass
                    elif msg.text in [".out all grup"]:
                      if msg._from in creator:
                        gid = ki.getGroupIdsJoined()
                        for i in gid:
                            cl.sendMessage(i,"Bot di paksa keluar oleh owner!")
                            cl.leaveGroup(i)
                            cl.sendMessage(msg.to,"Success left all group")

                    elif msg.text == self.resp + "invite on":
                        if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                            if wait2["Invi"] == False:
                                wait2["Invi"] = True
                                cl.sendMessage(msg.to, "send contact auto Invite on")
                    elif msg.text == self.resp + "invite off":
                        if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                            if wait2["Invi"] == True:
                                wait2["Invi"] = False
                                cl.sendMessage(msg.to, "auto Invite off")
                    elif msg.text in [".kickall"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        if msg.toType == 2:
                            group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            for x in nama:
                                if x not in creator:
                                    if x not in org["owner"]:
                                        if x not in org["admin"]:
                                            if x not in org["staff"]:
                                                try:
                                                    cl.kickoutFromGroup(msg.to,[x])
                                                except:
                                                    pass
                    elif msg.text in [".autojoin on"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        wait2["autoJoin"]=True
                        cl.sendMessage(msg.to,"Auto join in Activated")
                    elif msg.text in [".autojoin off"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        wait2["autoJoin"]=False
                        cl.sendMessage(msg.to,"Auto join not Active")
                    elif msg.text in [".bye"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        if msg.toType == 2:
                            ginfo = cl.getGroup(msg.to)
                            try:
                                cl.leaveGroup(msg.to)
                            except:
                                pass
                    elif msg.text == self.resp + "bye":
                      if msg._from in creator or msg._from in org["owner"]:
                        if msg.toType == 2:
                            ginfo = cl.getGroup(msg.to)
                            try:
                                cl.leaveGroup(msg.to)
                            except:
                                pass
                    elif msg.text in [".add owner on"]:
                        if msg._from in creator:
                            if wait2["addowner"] == False:
                                wait2["addowner"] = True
                                cl.sendMessage(msg.to, "Please send Contact for add")
                            else:
                                cl.sendMessage(msg.to, "send Contact for add")
                    elif msg.text in [".add owner off"]:
                        if msg._from in creator:
                            if wait2["addowner"] == True:
                                wait2["addowner"] = False
                                cl.sendMessage(msg.to, "Add owner was off")
                            else:
                                cl.sendMessage(msg.to, "Was off")
                    elif msg.text in [".del owner on"]:
                        if msg._from in creator:
                            if wait2["delowner"] == False:
                                wait2["delowner"] = True
                                cl.sendMessage(msg.to, "Please send Contact for Removed")
                            else:
                                cl.sendMessage(msg.to, "Was on,, Please send Contact for.Removed")
                    elif msg.text in [".del owner off"]:
                        if msg._from in creator:
                            if wait2["delowner"] == True:
                                wait2["delowner"] = False
                                cl.sendMessage(msg.to, "Removed owner was off")
                            else:
                                cl.sendMessage(msg.to, "Was off")
                    elif msg.text in [".clear owner"]:
                      if msg._from in creator:
                        org["owner"] = {}
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to,"Succes clear")
                    elif msg.text == self.resp + "owner":
                      if msg._from in creator:
                        if org["owner"] == {}:
                            cl.sendMessage(msg.to,"empty Tlist")
                        else:
                            mc = []
                            for mi_d in org["owner"]:
                                mc.append(mi_d)
                            pass
                            cban = cl.getContacts(mc)
                            nban = []
                            for x in range(len(cban)):
                                nban.append(cban[x].displayName)
                            pass
                            jo = "\n_ ".join(str(i) for i in nban)
                            cl.sendMessage(msg.to,"_====[ Owner List ]====_\n\n_ %s\n\n_====[ Total: %s ]====_"%(jo,str(len(cban))))
                    elif msg.text == self.resp + "admin":
                      if msg._from in creator:
                        if org["admin"] == {}:
                            cl.sendMessage(msg.to,"empty Tlist")
                        else:
                            mc = []
                            for mi_d in org["admin"]:
                                mc.append(mi_d)
                            pass
                            cban = cl.getContacts(mc)
                            nban = []
                            for x in range(len(cban)):
                                nban.append(cban[x].displayName)
                            pass
                            jo = "\n_ ".join(str(i) for i in nban)
                            cl.sendMessage(msg.to,"_====[ Admin List ]====_\n\n_ %s\n\n_====[ Total: %s ]====_"%(jo,str(len(cban))))
                    elif msg.text == self.resp + "staff":
                      if msg._from in creator:
                        if org["staff"] == {}:
                            cl.sendMessage(msg.to,"empty Tlist")
                        else:
                            mc = []
                            for mi_d in org["staff"]:
                                mc.append(mi_d)
                            pass
                            cban = cl.getContacts(mc)
                            nban = []
                            for x in range(len(cban)):
                                nban.append(cban[x].displayName)
                            pass
                            jo = "\n_ ".join(str(i) for i in nban)
                            cl.sendMessage(msg.to,"_====[ Staff List ]====_\n\n_ %s\n\n_====[ Total: %s ]====_"%(jo,str(len(cban))))

                    elif msg.text in [".add admin"]:
                        if msg._from in creator or msg._from in org["owner"]:
                            wait2["addadmin"]=True
                            cl.sendMessage(msg.to, "send contact")
                    elif msg.text in [".del admin"]:
                        if msg._from in creator or msg._from in org["owner"]:
                            wait2["deladmin"]=True
                            cl.sendMessage(msg.to, "send contact")
                    elif msg.text in [".clear admin"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        org["admin"] = {}
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to,"Succes clear")
                    elif msg.text in [".add staff"]:
                        if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                            wait2["addstaff"]=True
                            cl.sendMessage(msg.to, "send contact")
                    elif msg.text in [".del staff"]:
                        if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                            wait2["delstaff"]=True
                            cl.sendMessage(msg.to, "send contact")
                    elif msg.text in [".clear staff"]:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        org["staff"] = {}
                        with open('org.json', 'w') as fp:
                            json.dump(org, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to,"Succes clear")
                    elif msg.text in [".autojoin on"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        wait2["autoJoin"]=True
                        cl.sendMessage(msg.to,"Auto join in Activated")
                    elif msg.text in [".autojoin off"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        wait2["autoJoin"]=False
                        cl.sendMessage(msg.to,"Auto join not Active")
                    elif msg.text in [".cban"]:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        wait2['blacklist'] = {}
                        with open('wait2.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                        cl.sendMessage(to,"°done boss")
                    elif msg.text in [".addban"]:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                            wait2["ablacklist"]=True
                            cl.sendMessage(to, "please send contact")
                    elif msg.text in [".delban"]:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                            wait2["dblacklist"]=True
                            cl.sendMessage(to, "please send contact")

                    elif msg.text == self.resp + "banlist":
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        if wait2["blacklist"] == {}:
                            cl.sendMessage(to,"empty list")
                        else:
                            mc = "_====[ BLACKLIST ]====_\n"
                            for mi_d in wait2["blacklist"]:
                                mc += "\n_ "+cl.getContact(mi_d).displayName
                            cl.sendMessage(msg.to,mc + "\n_====[ BLACKLIST ]====_")
                    elif msg.text in [".sp"]:
                        if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                            start = time.time()
                            cl.sendMessage("u9d79f5031bc4c73a5054aa8b26c9d0c2", '.')
                            elapsed_time = time.time() - start
                            cl.sendMessage(msg.to, "%s second" % (elapsed_time))

                    elif msg.text in [".protect on"]:
                        if msg._from in creator or msg._from in org["owner"]:
                            pro["Proqr"][msg.to] = True
                            pro["Procancel"][msg.to] = True
                            pro["Proinvite"][msg.to] = True
                            pro["Autokick"][msg.to] = True
                            with open('pro.json','w') as fp:
                                json.dump(pro, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to,"High All Protection On")
                    elif msg.text in [".protect off"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        if msg.to in pro["Proqr"]:
                            try:
                                del pro["Proqr"][msg.to]
                            except:
                                pass
                        if msg.to in pro["Procancel"]:
                            try:
                                del pro["Procancel"][msg.to]
                            except:
                                pass
                        if msg.to in pro["Proinvite"]:
                            try:
                                del pro["Proinvite"][msg.to]
                            except:
                                pass
                        if msg.to in pro["Autokick"]:
                            try:
                                del pro["Autokick"][msg.to]
                            except:
                                pass
                        with open('pro.json','w') as fp:
                            json.dump(pro, fp, sort_keys=True, indent=4)
                        cl.sendMessage(msg.to,"All Protection Off")
                    elif msg.text == self.resp + "grup set":
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        md = ""
                        if msg.to in pro["Proqr"]: md+="_Protect grup : on_\n"
                        else: md +="_Protect grup : off_\n"
                        if msg.to in pro["Procancel"]: md+="_Protect cancel : on_\n"
                        else: md+= "_Protect cancel : off_\n"
                        if msg.to in pro["Proinvite"]: md+="_Protect invite : on_\n"
                        else: md+= "_Protect invite : off_\n"
                        if msg.to in pro["Autokick"]: md+="_Auto kick : on_\n"
                        else:md+="_Auto kick : off_\n"
                        if msg.to in pro["Proname"]: md+="_Protection Group Name : on_\n"
                        else: md+= "_Protection Group Name : off_\n"
                        cl.sendMessage(msg.to,"_========[ Grup set up ]========_\n\n"+ md +"_========[ Znf Bots ]========_")
                    elif self.resp + "gn" in msg.text:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        if msg.toType == 2:
                            X = cl.getGroup(msg.to)
                            X.name = msg.text.replace("gn","")
                            cl.updateGroup(X)

                    elif msg.text in ["Lockname on"]:
                        if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                            if msg.to in pro["Lockname"]:
                                cl.sendMessage(msg.to,"Name Group in Locked")
                            else:
                                pro["Lockname"][msg.to] = True
                                with open('pro.json','w') as fp:
                                    json.dump(pro, fp, sort_keys=True, indent=4)
                                pro["gname"][msg.to] = cl.getGroup(msg.to).name
                                with open('pro.json','w') as fp:
                                    json.dump(pro, fp, sort_keys=True, indent=4)
                                cl.sendMessage(msg.to,"Succes Locked Group Name")
                    elif msg.text in ["Lockname off"]:
                        if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                            if msg.to not in pro["Lockname"]:
                                cl.sendMessage(msg.to,"Name Group not in Locked")
                            else:
                                del pro["Lockname"][msg.to]
                                with open('pro.json','w') as fp:
                                    json.dump(pro, fp, sort_keys=True, indent=4)
                                del pro["gname"][msg.to]
                                with open('pro.json','w') as fp:
                                    json.dump(pro, fp, sort_keys=True, indent=4)
                                cl.sendMessage(msg.to,"Succes open Locked Group Name")

                    elif msg.text == self.resp +"mention":
                        group = cl.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        k = len(nama)//20
                        for a in range(k+1):
                            txt = u''
                            s=0
                            b=[]
                            for i in group.members[a*20 : (a+1)*20]:
                                b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                s += 7
                                txt += u'@Alin \n'
                            cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                    elif (".owner add" in msg.text):
                        if msg._from in creator:
                             key = eval(msg.contentMetadata["MENTION"])
                             key["MENTIONEES"][0]["M"]
                             targets = []
                             for x in key["MENTIONEES"]:
                                 targets.append(x["M"])
                             for target in targets:
                                 if target in org["owner"]:
                                     cl.sendMessage(msg.to,"Was owner..")
                                 else:
                                     try:
                                         org["owner"][target] = True
                                         with open('org.json','w') as fp:
                                             json.dump(org, fp, sort_keys=True, indent=4)
                                         cl.sendMessage(msg.to,"Succes add owner")
                                     except:
                                         pass
                    elif ".owner del " in msg.text:
                        if msg._from in creator:
                             key = eval(msg.contentMetadata["MENTION"])
                             key["MENTIONEES"][0]["M"]
                             targets = []
                             for x in key["MENTIONEES"]:
                                 targets.append(x["M"])
                             for target in targets:
                                 if target not in org["owner"]:
                                     cl.sendMessage(msg.to,"not in owner..")
                                 else:
                                     try:
                                         del org["owner"][target]
                                         with open('org.json','w') as fp:
                                             json.dump(org, fp, sort_keys=True, indent=4)
                                         cl.sendMessage(msg.to,"Succes remove owner")
                                     except:
                                         pass
                    elif ".admin add " in msg.text:
                      if msg._from in creator or msg._from in org["owner"]:
                           key = eval(msg.contentMetadata["MENTION"])
                           key["MENTIONEES"][0]["M"]
                           targets = []
                           for x in key["MENTIONEES"]:
                               targets.append(x["M"])
                           for target in targets:
                               if target in org["admin"]:
                                   cl.sendMessage(msg.to,"was admin")
                               else:
                                   try:
                                       org["admin"][target] = True
                                       with open('org.json','w') as fp:
                                           json.dump(org, fp, sort_keys=True, indent=4)
                                       cl.sendMessage(msg.to,"Succes remove admin")
                                   except:
                                       pass
                    elif ".admin del " in msg.text:
                      if msg._from in creator or msg._from in org["owner"]:
                           key = eval(msg.contentMetadata["MENTION"])
                           key["MENTIONEES"][0]["M"]
                           targets = []
                           for x in key["MENTIONEES"]:
                               targets.append(x["M"])
                           for target in targets:
                               if target not in org["admin"]:
                                   cl.sendMessage(msg.to,"not in admin")
                               else:
                                   try:
                                       del org["admin"][target]
                                       with open('org.json','w') as fp:
                                           json.dump(org, fp, sort_keys=True, indent=4)
                                       cl.sendMessage(msg.to,"Succes remove admin")
                                   except:
                                       pass
                    elif ".staff add " in msg.text:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                           key = eval(msg.contentMetadata["MENTION"])
                           key["MENTIONEES"][0]["M"]
                           targets = []
                           for x in key["MENTIONEES"]:
                               targets.append(x["M"])
                           for target in targets:
                               if target in org["staff"]:
                                   cl.sendMessage(msg.to,"was staff")
                               else:
                                   try:
                                       org["staff"][target] = True
                                       with open('org.json','w') as fp:
                                           json.dump(org, fp, sort_keys=True, indent=4)
                                       cl.sendMessage(msg.to,"Succes add staff")
                                   except:
                                       pass
                    elif ".staff del " in msg.text:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                           key = eval(msg.contentMetadata["MENTION"])
                           key["MENTIONEES"][0]["M"]
                           targets = []
                           for x in key["MENTIONEES"]:
                               targets.append(x["M"])
                           for target in targets:
                               if target not in org["staff"]:
                                   cl.sendMessage(msg.to,"not in staff")
                               else:
                                   try:
                                       del org["staff"][target]
                                       with open('org.json','w') as fp:
                                           json.dump(org, fp, sort_keys=True, indent=4)
                                       cl.sendMessage(msg.to,"Succes remove staff")
                                   except:
                                       pass
                    elif msg.text in [".rechat"]:
                      if msg._from in creator or msg._from in org["owner"] or msg._from in org["admin"]:
                        try:
                            cl.removeAllMessages(op.param2)
                            cl.sendMessage(to,"done")
                        except:
                            pass
                    elif msg.text in [".add on"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        wait2["message"]=True
                        cl.sendMessage(to,"autoAdd on")

                    elif msg.text in [".add off"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        wait2["message"]=False
                        cl.sendMessage(to,"autoAdd off")
                    elif msg.text in [".ticket on"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        wait2["autoJoinTicket"]=True
                        cl.sendMessage(to,"autoJoinTicket on")

                    elif msg.text in [".ticket off"]:
                      if msg._from in creator or msg._from in org["owner"]:
                        wait2["autoJoinTicket"]=False
                        cl.sendMessage(to,"autoJoinTicket off")
                    elif "/ti/g/" in msg.text.lower():
                        if msg._from in creator or msg._from in org["owner"]:
                          if wait2["autoJoinTicket"] == True:
                             link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                             links = link_re.findall(text)
                             n_links = []
                             for l in links:
                                 if l not in n_links:
                                    n_links.append(l)
                             for ticket_id in n_links:
                                 group = cl.findGroupByTicket(ticket_id)
                                 cl.acceptGroupInvitationByTicket(group.id,ticket_id)


        except:
            e = traceback.format()
            with open("e","a") as error:error.write("\n{}".format(e))
