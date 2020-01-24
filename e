
Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 147, in RECEIVE_MESSAGE
    if dzin.lower() == "refreshh" and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7"]:sendMention(msg.to, '╭──「 Serivce 」\n│Type : Restart bot login\n╰Success restart bot login @!','「 RESTART BOT LOGIN 」', [key1]);mystic.restart_program()
UnboundLocalError: local variable 'key1' referenced before assignment

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 147, in RECEIVE_MESSAGE
    if dzin.lower() == "refreshh" and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7"]:sendMention(msg.to, '╭──「 Serivce 」\n│Type : Restart bot login\n╰Success restart bot login @!','「 RESTART BOT LOGIN 」', [msg._from]);mystic.restart_program()
UnboundLocalError: local variable 'key1' referenced before assignment

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 66, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭──「 Serivce 」\n│Type : Help message\n│OWNER COMMANDS\n│1.) Adduser [name] [@]\n│2.) Deluser [name] [@]\n│3.) List user\n│4.) Runall\n│5.) Kilall\n│6.) Refreshh\n│USER COMMANDS\n│7.) Mystic login\n╰Creator : @!','「 HElP MESSAGE 」', ["uc7d319b7d2d38c35ef2b808e3a2aeed9"])
  File "pois.py", line 50, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/Test/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/Test/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/Test/akads/TalkService.py", line 6799, in sendMessage
    return self.recv_sendMessage()
  File "/root/Test/akads/TalkService.py", line 6833, in recv_sendMessage
    raise result.e
akads.ttypes.TalkException: TalkException(code=0, reason='invalid mention.', parameterMap=None)

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 66, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭──「 Serivce 」\n│Type : Help message\n│OWNER COMMANDS\n│1.) Adduser [name] [@]\n│2.) Deluser [name] [@]\n│3.) List user\n│4.) Runall\n│5.) Kilall\n│6.) Refreshh\n│USER COMMANDS\n│7.) Mystic login\n╰Creator : @!','「 HElP MESSAGE 」', ["uc7d319b7d2d38c35ef2b808e3a2aeed9"])
  File "pois.py", line 50, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/Test/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/Test/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/Test/akads/TalkService.py", line 6799, in sendMessage
    return self.recv_sendMessage()
  File "/root/Test/akads/TalkService.py", line 6833, in recv_sendMessage
    raise result.e
akads.ttypes.TalkException: TalkException(code=0, reason='invalid mention.', parameterMap=None)

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 120, in RECEIVE_MESSAGE
    else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
ValueError: year 484688845 is out of range

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 147, in RECEIVE_MESSAGE
    if dzin.lower() == "refreshh" and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7"]:sendMention(msg.to, '╭──「 Serivce 」\n│Type : Restart bot login\n╰Success restart bot login @!','「 RESTART BOT LOGIN 」', [msg._from]);mystic.restart_program()
  File "pois.py", line 50, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/Test/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/Test/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/Test/akads/TalkService.py", line 6799, in sendMessage
    return self.recv_sendMessage()
  File "/root/Test/akads/TalkService.py", line 6833, in recv_sendMessage
    raise result.e
akads.ttypes.TalkException: TalkException(code=0, reason='invalid mention.', parameterMap=None)

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 66, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭──「 Serivce 」\n│Type : Help message\n│OWNER COMMANDS\n│1.) Adduser [name] [@]\n│2.) Deluser [name] [@]\n│3.) List user\n│4.) Runall\n│5.) Kilall\n│6.) Refreshh\n│USER COMMANDS\n│7.) Mystic login\n╰Creator : @!','「 HElP MESSAGE 」', ["uc7d319b7d2d38c35ef2b808e3a2aeed9"])
  File "pois.py", line 50, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/Test/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/Test/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/Test/akads/TalkService.py", line 6799, in sendMessage
    return self.recv_sendMessage()
  File "/root/Test/akads/TalkService.py", line 6833, in recv_sendMessage
    raise result.e
akads.ttypes.TalkException: TalkException(code=0, reason='invalid mention.', parameterMap=None)

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 147, in RECEIVE_MESSAGE
    if dzin.lower() == "refreshh" and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7"]:sendMention(msg.to, '╭──「 Serivce 」\n│Type : Restart bot login\n╰Success restart bot login @!','「 RESTART BOT LOGIN 」', [msg._from]);mystic.restart_program()
  File "pois.py", line 50, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/Test/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/Test/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/Test/akads/TalkService.py", line 6799, in sendMessage
    return self.recv_sendMessage()
  File "/root/Test/akads/TalkService.py", line 6833, in recv_sendMessage
    raise result.e
akads.ttypes.TalkException: TalkException(code=0, reason='invalid mention.', parameterMap=None)

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 120, in RECEIVE_MESSAGE
    else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
ValueError: year 484688845 is out of range

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 75, in RECEIVE_MESSAGE
    wait['name'][nama] =  {"mid":key1,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
UnboundLocalError: local variable 'key1' referenced before assignment

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 120, in RECEIVE_MESSAGE
    else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
ValueError: year 484688845 is out of range

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 120, in RECEIVE_MESSAGE
    else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
ValueError: year 484688845 is out of range

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 121, in RECEIVE_MESSAGE
    if wait['name'][wait['info'][a]]["name"] == "":cd = "None."
KeyError: 'name'

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 122, in RECEIVE_MESSAGE
    if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
KeyError: 'user'

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 122, in RECEIVE_MESSAGE
    if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
KeyError: 'user'

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 122, in RECEIVE_MESSAGE
    if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
KeyError: 'user'

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 122, in RECEIVE_MESSAGE
    if wait['name'][wait['info'][a]]["user"] == "":cd = "None."
KeyError: 'user'

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 126, in RECEIVE_MESSAGE
    sendMention(msg.to, msgas,'「 LIST USER 」', h)
  File "pois.py", line 27, in sendMention
    raise Exception("Invalid mids")
Exception: Invalid mids

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 67, in RECEIVE_MESSAGE
    if dzin.lower().startswith("$ ") and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:q=dzin.replace("$ ","");s=os.popen(query);p=s.read();sendMention(msg.to, p,'「 OS SYSTEM 」', [msg._from])
NameError: name 'query' is not defined

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 67, in RECEIVE_MESSAGE
    if dzin.lower().startswith("$ ") and msg._from in ["uc7d319b7d2d38c35ef2b808e3a2aeed9","ub4974c6489c969402713a974b568ee9e","uaca55463c423c3632012598148691da7","u23e3b0e57f43ea3924242ef7a72bda06"]:q=dzin.replace("$ ","");s=os.popen(query);p=s.read();sendMention(msg.to, p,'「 OS SYSTEM 」', [msg._from])
NameError: name 'query' is not defined

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 150, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭──「 Service 」\n│Type : Kill all selfbot user\n╰Success kill all selfbot user @!','「 KILL ALL SELFBOT 」', [key1])
UnboundLocalError: local variable 'key1' referenced before assignment

Traceback (most recent call last):
  File "/root/Test/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 139, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭──「 Service 」\n│Type : Run all selfbot user\n╰Success run all selfbot user @!','「 RUN ALL SELFBOT 」', [key1])
UnboundLocalError: local variable 'key1' referenced before assignment

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 211, in RECEIVE_MESSAGE
    if dzin.lower() == "relog" and msg._from in ['u2286e272840491415e82447163dadf6c']:mystic.sendMessage(msg.to, 'Sukses memulai ulang.','「 BOT LOGIN 」', [msg._from]);mystic.restart_program()
  File "/root/23/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/23/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/23/akads/TalkService.py", line 6798, in sendMessage
    self.send_sendMessage(seq, message)
  File "/root/23/akads/TalkService.py", line 6815, in send_sendMessage
    args.write(self._oprot)
  File "/root/23/akads/TalkService.py", line 34952, in write
    self.message.write(oprot)
  File "/root/23/akads/ttypes.py", line 8345, in write
    oprot.writeI32(self.contentType)
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TCompactProtocol.py", line 42, in nested
    return func(self, *args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TCompactProtocol.py", line 263, in writeI32
    self.__writeVarint(makeZigZag(i32, 32))
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TCompactProtocol.py", line 52, in makeZigZag
    checkIntegerLimits(n, bits)
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TProtocol.py", line 409, in checkIntegerLimits
    elif bits == 32 and (i < -2147483648 or i > 2147483647):
TypeError: '<' not supported between instances of 'list' and 'int'

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 211, in RECEIVE_MESSAGE
    if dzin.lower() == "relog" and msg._from in ['u2286e272840491415e82447163dadf6c']:mystic.sendMessage(msg.to, 'Sukses memulai ulang.','「 BOT LOGIN 」', [msg._from]);mystic.restart_program()
  File "/root/23/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/23/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/23/akads/TalkService.py", line 6798, in sendMessage
    self.send_sendMessage(seq, message)
  File "/root/23/akads/TalkService.py", line 6811, in send_sendMessage
    self._oprot.writeMessageBegin('sendMessage', TMessageType.CALL, self._seqid)
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TCompactProtocol.py", line 156, in writeMessageBegin
    assert self.state == CLEAR
AssertionError

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 94, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭─☾ Supported by SmileBots☽─\n┊\n┊○ : Staff/Owner Only\n┊● : All Can Use!\n┊\n┊● smilelogin\n┊○ +user 「filename」「mention」\n┊○ -user 「filename」 「mention」\n┊○ Usernames\n┊○ Usertimes\n┊○ respon\n┊○ /relogin\n┊○ /killme\n┊○ /restart\n┊○ bye\n┊\n╰─☾ Contact me at @! ☽─','「 HElP MESSAGE 」', ['u2286e272840491415e82447163dadf6c'])
  File "pois.py", line 57, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/23/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/23/linepys/client.py", line 50, in getProfile
    return self._client.getProfile()
  File "/root/23/akads/TalkService.py", line 4048, in getProfile
    self.send_getProfile()
  File "/root/23/akads/TalkService.py", line 4052, in send_getProfile
    self._oprot.writeMessageBegin('getProfile', TMessageType.CALL, self._seqid)
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TCompactProtocol.py", line 156, in writeMessageBegin
    assert self.state == CLEAR
AssertionError

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 89, in RECEIVE_MESSAGE
    mystic.sendMessage(msg.to,'Waiting..')
  File "/root/23/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/23/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/23/akads/TalkService.py", line 6798, in sendMessage
    self.send_sendMessage(seq, message)
  File "/root/23/akads/TalkService.py", line 6811, in send_sendMessage
    self._oprot.writeMessageBegin('sendMessage', TMessageType.CALL, self._seqid)
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TCompactProtocol.py", line 156, in writeMessageBegin
    assert self.state == CLEAR
AssertionError

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 211, in RECEIVE_MESSAGE
    if dzin.lower() == "relog" and msg._from in ['u2286e272840491415e82447163dadf6c']:mystic.sendMessage(msg.to, 'Sukses memulai ulang.','「 BOT LOGIN 」', [msg._from]);mystic.restart_program()
  File "/root/23/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/23/linepys/client.py", line 167, in sendMessage
    return self._client.sendMessage(self._messageReq[to], msg)
  File "/root/23/akads/TalkService.py", line 6798, in sendMessage
    self.send_sendMessage(seq, message)
  File "/root/23/akads/TalkService.py", line 6815, in send_sendMessage
    args.write(self._oprot)
  File "/root/23/akads/TalkService.py", line 34952, in write
    self.message.write(oprot)
  File "/root/23/akads/ttypes.py", line 8345, in write
    oprot.writeI32(self.contentType)
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TCompactProtocol.py", line 42, in nested
    return func(self, *args, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TCompactProtocol.py", line 263, in writeI32
    self.__writeVarint(makeZigZag(i32, 32))
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TCompactProtocol.py", line 52, in makeZigZag
    checkIntegerLimits(n, bits)
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TProtocol.py", line 409, in checkIntegerLimits
    elif bits == 32 and (i < -2147483648 or i > 2147483647):
TypeError: '<' not supported between instances of 'list' and 'int'

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 94, in RECEIVE_MESSAGE
    sendMention(msg.to, '╭─☾ Supported by SmileBots☽─\n┊\n┊○ : Staff/Owner Only\n┊● : All Can Use!\n┊\n┊● smilelogin\n┊○ +user 「filename」「mention」\n┊○ -user 「filename」 「mention」\n┊○ Usernames\n┊○ Usertimes\n┊○ respon\n┊○ /relogin\n┊○ /killme\n┊○ /restart\n┊○ bye\n┊\n╰─☾ Contact me at @! ☽─','「 HElP MESSAGE 」', ['u2286e272840491415e82447163dadf6c'])
  File "pois.py", line 57, in sendMention
    mystic.sendMessage(to, textx, {'AGENT_LINK': 'line://ti/p/~{}'.format(mystic.profile.userid),'AGENT_ICON': "http://dl.profile.line-cdn.net/" + mystic.getProfile().picturePath,'AGENT_NAME': ps,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
  File "/root/23/linepys/client.py", line 17, in checkLogin
    return func(*args, **kwargs)
  File "/root/23/linepys/client.py", line 50, in getProfile
    return self._client.getProfile()
  File "/root/23/akads/TalkService.py", line 4048, in getProfile
    self.send_getProfile()
  File "/root/23/akads/TalkService.py", line 4052, in send_getProfile
    self._oprot.writeMessageBegin('getProfile', TMessageType.CALL, self._seqid)
  File "/usr/local/lib/python3.6/dist-packages/thrift/protocol/TCompactProtocol.py", line 156, in writeMessageBegin
    assert self.state == CLEAR
AssertionError

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 123, in RECEIVE_MESSAGE
    os.system('screen -S %s -dm python3 %s.py' %(us,us))
UnboundLocalError: local variable 'us' referenced before assignment

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 123, in RECEIVE_MESSAGE
    os.system('screen -S %s -dm python3 %s.py' %(us,us))
UnboundLocalError: local variable 'us' referenced before assignment

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 130, in RECEIVE_MESSAGE
    wait['name'][us]["token"] = res.authToken
UnboundLocalError: local variable 'res' referenced before assignment

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 131, in RECEIVE_MESSAGE
    cpfile(us,wait['name'][us]["token"])
UnboundLocalError: local variable 'us' referenced before assignment

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 131, in RECEIVE_MESSAGE
    cpfile(wait['name']["token"])
KeyError: 'token'

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 131, in RECEIVE_MESSAGE
    cpfile(wait['name'])
TypeError: cpfile() missing 1 required positional argument: 'tt'

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 131, in RECEIVE_MESSAGE
    cpfile(nama ,info)
NameError: name 'info' is not defined

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 131, in RECEIVE_MESSAGE
    cpfile(nama)
TypeError: cpfile() missing 1 required positional argument: 'tt'

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 131, in RECEIVE_MESSAGE
    copyDrectory(name)
NameError: name 'copyDrectory' is not defined

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 131, in RECEIVE_MESSAGE
    cpfile('name')
TypeError: cpfile() missing 1 required positional argument: 'tt'

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 238, in RECEIVE_MESSAGE
    wait['name'][us]["token"] = res.authToken
UnboundLocalError: local variable 'res' referenced before assignment

Traceback (most recent call last):
  File "/root/23/linepys/poll.py", line 27, in execute
    self.OpInterrupt[op.type](op)
  File "pois.py", line 238, in RECEIVE_MESSAGE
    wait['name'][us]["token"] = res.authToken
UnboundLocalError: local variable 'res' referenced before assignment
