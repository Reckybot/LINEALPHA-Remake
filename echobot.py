

            elif msg.text in ["Ar Bot 2","Ar bot 2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                kk.sendMessage(msg)
                print "[Command]Bot 2 executed"

            elif msg.text in ["Ar Bot 3","Ar bot 3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
                print "[Command]Bot 3 executed"

            elif msg.text in ["Ar Bot 4","Ar bot 4"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                print "[Command]Bot 4 executed"

            elif msg.text in ["Ar Bot 5","Ar bot 5"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kg.sendMessage(msg)
                print "[Command]Bot 5 executed"
#-----------------------[Cancel invitation Section]------------------------
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:                    
                    X = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Canceling all pending(s) invitation")
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        print "[Command]Cancel executed"
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"This group doesn't have any pending invitation")
                            print "[Command]Group don't have pending invitation"
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "Cancel executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Group link Section]------------------------                        
            elif msg.text in ["Ar Glink off","Ar Link off","Ar glink off","Ar link off"]:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned off")
                            print "[Command]Glink off executed"
                        else:
                            cl.sendText(msg.to,"Already turned off")
                            print "[Command]Glink off executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Glink off executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Ar Glink on","Ar Link on","Ar glink on","Ar link on"]:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned on")
                            print "[Command]Glink on executed"
                        else:
                            cl.sendText(msg.to,"Already turned on")
                            print "[Command]Glink on executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Glink on executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Group info Section]------------------------
            elif msg.text in ["Ar Ginfo","Ar ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                        print "[Command]Ginfo executed"
                    else:
                        random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                        print "[Command]Ginfo executed"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Ginfo executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Bot/User/Group ID Section]------------------------
            elif msg.text in ["Ar Gid","Ar gid"]:
                cl.sendText(msg.to,msg.to)
                print "[Command]Gid executed"
            elif msg.text in ["Ar Mid all","Ar mid all"]:
                cl.sendText(msg.to,"[Ardh-]Bot(s) ID\n[Ardh-]BOT1\n" + mid + "\n\n[Ardh-]BOT2\n" + Amid + "\n\n[Ardh-]BOT3\n" + Bmid + "\n\n[Ardh-]BOT4\n" + Cmid + "\n\n[Ardh-]BOT5\n" + Dmid)
                print "[Command]Mid executed"
            elif msg.text in ["Ar Mid 1","Ar mid 1"]:
                cl.sendText(msg.to,mid)
                print "[Command]Mid 1 executed"
            elif msg.text in ["Ar Mid 2","Ar mid 2"]:
                kk.sendText(msg.to,Amid)
                print "[Command]Mid 2 executed"
            elif msg.text in ["Ar Mid 3","Ar mid 3"]:
                ki.sendText(msg.to,Bmid)
                print "[Command]Mid 3 executed"
            elif msg.text in ["Ar Mid 4","Ar mid 4"]:
                kc.sendText(msg.to,Cmid)
                print "[Command]Mid 4 executed"
            elif msg.text in ["Ar Mid 5","Ar mid 5"]:
                kc.sendText(msg.to,Dmid)
                print "[Command]Mid 5 executed"
            elif msg.text in ["Ar Yid","Ar yid"]:
                cl.sendText(msg.to,msg.from_)
                print "[Command]Yid executed"
#-----------------------[Send Contact Section]------------------------
            elif "Ar Contact" in msg.text:
                mmid = msg.text.replace("Ar Contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                print "[Command]Contact executed"
            elif "Ar contact" in msg.text:
                mmid = msg.text.replace("Ar contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                print "[Command]Contact executed"
#-----------------------[Auto Join Section]------------------------
            elif msg.text in ["Ar Join on","Ar join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already on")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"Auto join already on")
                        print "[Command]Join on executed"
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned on")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"Auto join turned on")
                        print "Join on executed"
            elif msg.text in ["Ar Join off","Ar join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto join already off")
                        print "[Command]Join off executed"
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto join turned off")
                        print "[Command]Join off executed"
#-----------------------[Group Url Section]------------------------
            elif msg.text in ["Ar Gurl","Ar gurl"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        x = cl.getGroup(msg.to)
                        if x.preventJoinByTicket == True:
                            x.preventJoinByTicket = False
                            cl.updateGroup(x)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"line://ti/g/" + gurl)
                        print "[Command]Gurl executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                        print "[Command]Gurl executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[All bots join group Section]------------------------
            elif msg.text in ["Ar Join all","Ar join all"]:
                if msg.from_ in admin:
                    try:
                        ginfo = cl.getGroup(msg.to)
                        ginfo.preventJoinByTicket = False
                        cl.updateGroup(ginfo)

                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)

                        ginfo = random.choice(KAC).getGroup(msg.to)
                        ginfo.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(ginfo)
                    except:
                        print "Somethings wrong with the url"
                    print "[Command]Join all executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
#-----------------------[Bot(s) Leave Section]------------------------
            elif msg.text in ["Ar Bye all","Ar bye all"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            ki.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            kg.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye all executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Ar Bye bot 1","Ar bye bot 1"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 1 executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Ar Bye bot 2","Ar bye bot 2"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kk.getGroup(msg.to)
                        try:
                            kk.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 2 executed"
                    else:
                        kk.sendText(msg.to,"Command denied.")
                        kk.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Ar Bye bot 3","Ar bye bot 3"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = ki.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 3 executed"
                    else:
                        ki.sendText(msg.to,"Command denied.")
                        ki.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Ar Bye bot 4","Ar bye bot 4"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kc.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 4 executed"
                    else:
                        kc.sendText(msg.to,"Command denied.")
                        kc.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Ar Bye bot 5","Ar bye bot 5"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kg.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 5 executed"
                    else:
                        kg.sendText(msg.to,"Command denied.")
                        kg.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Cleanse Section (USE AT YOUR OWN RISK!)]------------------------
            elif msg.text in ["Ar Cleanse","Ar cleanse"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Cleanse executing"
                        _name = msg.text.replace("Cleanse","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        kk.sendText(msg.to,"Group cleansing begin")
                        kc.sendText(msg.to,"Goodbye :)")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        # --------------[Bot and Admin MID]----------------
                        targets.remove(adminMID)
                        targets.remove(mid)
                        targets.remove(Amid)
                        targets.remove(Bmid)
                        targets.remove(Cmid)
                        targets.remove(Dmid)
                        # --------------[Bot and Admin MID]----------------
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    klist=[ki,kk,kc,cl,kg]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group cleansed")
                        print "[Command]Cleanse executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Ban/Unban Section]------------------------
            elif "Ar Ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Command]Ban executed"
                            _name = msg.text.replace("Ar Ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            gs = kg.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "Ar Unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Unban executed"
                        _name = msg.text.replace("Ar Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif "Ar ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Command]Ban executed"
                            _name = msg.text.replace("Ar ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            gs = kg.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "Ar unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Unban executed"
                        _name = msg.text.replace("Ar unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Ar Ban","Ar ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Ban")
                    print "[Command]Ban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Ar Unban","Ar unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Unban")
                    print "[Command]Unban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Ar Banlist","Ar banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No user is Blacklisted")
                else:
                    cl.sendText(msg.to,"Blacklisted user(s)")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Banlist executed"
#-----------------------[Bot Speak Section]------------------------
            elif "Ar Bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("Ar Bc ","")
                    random.choice(KAC).sendText(msg.to,(bctxt))
                    print "[Command]Bc executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif "Ar bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("Ar bc ","")
                    cl.sendText(msg.to,(bctxt))
                    print "[Command]Bc executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Bot speed test Section]------------------------
            elif msg.text in ["Ar Sp all","Ar Speed all","Ar sp all","Ar speed all"]:
                if msg.from_ in staff:

                    start = time.time()
                    cl.sendText(msg.to, "Bot 1 Processing Request")                    
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))

                    start2 = time.time()
                    kk.sendText(msg.to, "Bot 2 Processing Request")                    
                    elapsed_time2 = time.time() - start2
                    kk.sendText(msg.to, "%sseconds" % (elapsed_time2))
                    
                    start3 = time.time()
                    ki.sendText(msg.to, "Bot 3 Processing Request")                    
                    elapsed_time3 = time.time() - start3
                    ki.sendText(msg.to, "%sseconds" % (elapsed_time3))
                    
                    start4 = time.time()
                    kc.sendText(msg.to, "Bot 4 Processing Request")                    
                    elapsed_time4 = time.time() - start4
                    kc.sendText(msg.to, "%sseconds" % (elapsed_time4))
                    
                    start5 = time.time()
                    kg.sendText(msg.to, "Bot 5 Processing Request")                    
                    elapsed_time5 = time.time() - start5
                    kg.sendText(msg.to, "%sseconds" % (elapsed_time5))
                    print "[Command]Speed all executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Sp 1","Ar Speed 1","Ar sp 1","Ar speed 1"]:
                if msg.from_ in staff: 
                    start = time.time()                   
                    cl.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 1 executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Sp 2","Ar Speed 2","Ar sp 2","Ar speed 2"]:
                if msg.from_ in staff:
                    start = time.time()                    
                    kk.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    kk.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 2 executed"
                else:
                    kk.sendText(msg.to,"Command denied.")
                    kk.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Sp 3","Ar Speed 3","Ar sp 3","Ar speed 3"]:
                if msg.from_ in staff:
                    start = time.time()                   
                    ki.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 3 executed"
                else:
                    ki.sendText(msg.to,"Command denied.")
                    ki.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Sp 4","Ar Speed 4","Ar sp 4","Ar speed 4"]:
                if msg.from_ in staff: 
                    start = time.time()                   
                    kc.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    kc.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 4 executed"
                else:
                    kc.sendText(msg.to,"Command denied.")
                    kc.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Sp 5","Ar Speed 5","Ar sp 5","Ar speed 5"]:
                if msg.from_ in staff:    
                    start = time.time()                
                    kg.sendText(msg.to, "Progress...")                                       
                    elapsed_time = time.time() - start
                    kg.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 5 executed"
                else:
                    kc.sendText(msg.to,"Command denied.")
                    kc.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Auto Cancel Section]------------------------
            elif "Ar staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Ar staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Ar Staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Ar Staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Ar staff remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Ar staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Ar Staff remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Ar Staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Ar Stafflist","Ar stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------[Auto cancel Section]------------------------
            elif msg.text in ["Ar Cancel off","Ar cancel off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == True:
                        cancelinvite["autoCancel"] = False
                        cl.sendText(msg.to, "Auto Cancel turned off")
                        print "[Command]Cancel off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Cancel off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Cancel on","Ar cancel on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == False:
                        cancelinvite["autoCancel"] = True
                        cl.sendText(msg.to, "Auto Cancel turned on")
                        print "[Command]Cancel on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned on")
                        print "[Command]Cancel on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Url off","Ar url off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == True:
                        cancelinvite["autoCancelUrl"] = False
                        cl.sendText(msg.to, "Auto Cancel Url turned off")
                        print "[Command]Url off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Url off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Url on","Ar url on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == True:
                        cancelinvite["autoCancelUrl"] = False
                        cl.sendText(msg.to, "Auto Cancel Url turned off")
                        print "[Command]Url on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Url on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Misc Section]-------------------------------------------
            elif "Ar random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        strnum = msg.text.replace("Ar random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.05)
                                group.name = name
                                random.choice(KAC).updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                        print "[Command]Random executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

            elif "Ar Random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        strnum = msg.text.replace("Ar Random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.01)
                                group.name = name
                                cl.updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                        print "[Command]Random executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Absen","Ar absen"]:
                if msg.from_ in staff:
                    cl.sendText(msg.to, "Hadir")
                    kk.sendText(msg.to, "Hadir")
                    ki.sendText(msg.to, "Hadir")
                    kc.sendText(msg.to, "Hadir")
                    kg.sendText(msg.to, "Hadir")
                    print "[Command]Absen executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            #VPS STUFF - VPS NEEDED TO RUN THIS COMMAND :)
            # elif msg.text in ["Ar Kernel","Ar kernel"]:
            #     if msg.from_ in admin:
            #         botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
            #         cl.sendText(msg.to, botKernel)
            #         print "[Command]Kernel executed"
            #     else:
            #         cl.sendText(msg.to,"Command denied.")
            #         cl.sendText(msg.to,"Admin permission required.")
            #         print "[Error]Command denied - Admin permission required"

            # elif "Ar Stalk " in msg.text:
            #     print "[Command]Stalk executing"
            #     stalkID = msg.text.replace("Ar Stalk ","")
            #     subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
            #     files = glob.glob("tmp/*.jpg")
            #     for file in files:
            #         os.rename(file,"tmp/tmp.jpg")
            #     fileTmp = glob.glob("tmp/tmp.jpg")
            #     if not fileTmp:
            #         cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
            #         print "[Command]Stalk executed - no image found"
            #     else:
            #         image = upload_tempimage(client)
            #         cl.sendText(msg.to, format(image['link']))
            #         print "[Command]Stalk executed - success"

            # elif "Ar stalk " in msg.text:
            #     print "[Command]Stalk executing"
            #     stalkID = msg.text.replace("Ar stalk ","")
            #     subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
            #     files = glob.glob("tmp/*.jpg")
            #     for file in files:
            #         os.rename(file,"tmp/tmp.jpg")
            #     fileTmp = glob.glob("tmp/tmp.jpg")
            #     if not fileTmp:
            #         cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
            #         print "[Command]Stalk executed - no image found"
            #     else:
            #         image = upload_tempimage(client)
            #         cl.sendText(msg.to, format(image['link']))
            #         subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
            #         print "[Command]Stalk executed - success"

            elif "Ar img" in msg.text:
                path = "a.png"
                try:
                    cl.sendImage(msg.to, path)
                except:
                    cl.sendText(msg.to, "Failed to upload image")        

            else:
                if cl.getGroup(msg.to).preventJoinByTicket == False:
                    cl.reissueGroupTicket(msg.to)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                else:
                    if msg.from_ in Bots:
                        pass
                    else:
                        print "No Action"
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = kk.getProfile()
                profile2.displayName = wait["cName2"]
                kk.updateProfile(profile2)

                profile3 = ki.getProfile()
                profile3.displayName = wait["cName3"]
                ki.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = kg.getProfile()
                profile5.displayName = wait["cName5"]
                kg.updateProfile(profile5)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
