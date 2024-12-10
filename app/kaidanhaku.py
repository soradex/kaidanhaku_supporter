import flet as ft 
import random as rd

def main(page: ft.Page): 
    page.scroll=True
    def add_clicked(e):
        new_task.data.append(new_task.value)
        page.add(ft.Text("キーワード."+str(len(new_task.data))+" -> "+new_task.value))
        page.update()
    def add_clicked_player(e):
        players.data.append(players.value)
        page.add(ft.Text("プレイヤー."+str(len(players.data))+" -> "+players.value))

        page.update()
    def start(e):

        #ファンタイベント
        def close_dlg(e):
            err_dlg.open = False
            page.update()
        
        err_dlg = ft.AlertDialog(title=ft.Text("待つんだ！"),modal=True,content=ft.Text("好きなファンタの味を言え！！ それがルールだ！"),actions=[ft.TextButton("OK!",on_click=close_dlg),],actions_alignment=ft.MainAxisAlignment.END,)
        page.dialog = err_dlg
        err_dlg.open = True
        page.update()

        page.title = "怪談白物語-プレイ" 
        hontex=ft.Text(maintext.value,data=maintext.value)
        #ボタンを押された時の関数
        def change(e):
            dice=str(rd.randint(1,6))
            chalenge_pl=pl_inpo[pls.index(dd.value)]
            if dice==chalenge_pl[2]:
                chalenge_pl[1]-=1
                if chalenge_pl[1]==0:
                    if chalenge_pl[0]=="無職":
                        log.controls.append(ft.Text(dd.value+"  "+before.value+" => "+after.value+"  "+dice+" 失敗 残りHP->"+str(chalenge_pl[1])+"死亡 おまえ、むーしょく"))
                    else:
                        log.controls.append(ft.Text(dd.value+"  "+before.value+" => "+after.value+"  "+dice+" 失敗 残りHP->"+str(chalenge_pl[1])+"死亡"))
                    if chalenge_pl[0]=="脚本家":
                        hontex.value=hontex.value.replace(before.value,""+after.value+"")
                        texts.controls.append(hontex)
                    page.update()
                else:
                    if chalenge_pl[0]=="無職":
                        log.controls.append(ft.Text(dd.value+"  "+before.value+" => "+after.value+"  "+dice+" 失敗 残りHP->"+str(chalenge_pl[1])+" おまえ、むーしょく"))
                        page.update()
                    else:
                        log.controls.append(ft.Text(dd.value+"  "+before.value+" => "+after.value+"  "+dice+" 失敗 残りHP->"+str(chalenge_pl[1])))
                        page.update()
                if chalenge_pl[0]=="編集者":
                    log.controls.append(ft.Text("キーワード:"+keywords[0]))
            else:
                if chalenge_pl[0]=="無職":
                    log.controls.append(ft.Text(dd.value+"  "+before.value+" => "+after.value+"  "+dice+" 成功 おまえ、むーしょく"))
                    pass
                elif chalenge_pl[0]=="呪術師":
                    log.controls.append(ft.Text(dd.value+"  "+before.value+" => "+after.value+"  "+dice+" 成功"))
                    x=0
                    higai=""
                    for i in pl_inpo:
                        if i[2]==dice:
                            i[1]-=1
                            higai+=pls[x]
                        x+=1
                    log.controls.append(ft.Text(higai))

                
                log.controls.append(ft.Text(dd.value+"  "+before.value+" => "+after.value+"  "+dice+" 成功"))
                if before.value in keywords:
                    log.controls.append(ft.Text(before.value+" はキーワードです!"))
                    keywords.remove(before.value)
                hontex.value=hontex.value.replace(before.value,""+after.value+"")
                texts.controls.append(hontex)
                if chalenge_pl[0]=="科学者":
                    page.dialog = twochance_dlg
                    twochance_dlg.open = True
            if chalenge_pl[0]=="呪術師":
                higai=""
                x=0
                for i in pl_inpo:
                    if i[2]==diece and (not pls[x]==dd.value):
                        print(pls[x])
                        i[1]-=1
                        higai+=pls[x]+" "
                    x+=1
                log.controls.append(ft.Text("あなたのせいで："+higai+"たちが被害を受けました 謝ってください"))
                chalenge_pl[1]+=1
            page.update()
        def close_and_change(e):
            hontex.value=hontex.value.replace(before.value,""+after.value+"")
            log.controls.append(ft.Text(dd.value+"/科学者能力  "+before.value+" => "+after.value+"   自動成功"))
            texts.controls.append(hontex)
            twochance_dlg.open = False
            page.update()

        
        texts.controls.append(hontex)
        start_ok.data=1
        #これまでのをぶっ殺す
        for i in range(len(page.controls)):
            page.controls.pop()
        #名前をドロップダウンに追加
        dd_in=[]
        pls=[]
        for i in players.data:
            i=i.split()
            i=i[0]
            pls.append(i)
            dd_in.append(ft.dropdown.Option(i))

        dd = ft.Dropdown(width=100,options=dd_in,)
        change_button=ft.FloatingActionButton(icon=ft.icons.CHANGE_CIRCLE, on_click=change)

        before = ft.TextField(hint_text="変える前の物",width=200)
        after = ft.TextField(hint_text="変えた後の物",width=200)

        twochance_dlg = ft.AlertDialog(title=ft.Text("もう１っこは何を変える?(買えないなら空白のままクリックしてね)"),modal=True,content=ft.Row([before,after]),actions=[ft.TextButton("変更",on_click=close_and_change),],actions_alignment=ft.MainAxisAlignment.END,)

        pl_inpo=[]
        keywords=new_task.data
        page.add(ft.Text("「"+sinarioname.value+"」",size=30))
        page.add(ft.Text("職業1欄",size=25))
        for i in players.data:
            i=i.split()
            diece=i[1]
            i=i[0]
            shoku=rd.randint(1,6)
            match shoku:
                case 1:
                    pl_inpo.append(["脚本家",3,diece])
                    page.add(ft.Text(i+":脚本家/"+"死ぬダイス:"+str(diece)))
                case 2:
                    pl_inpo.append(["編集者",3,diece])
                    page.add(ft.Text(i+":編集者/"+"死ぬダイス:"+str(diece)))
                case 3:
                    pl_inpo.append(["霊媒師",4,diece])
                    page.add(ft.Text(i+":霊媒師/"+"死ぬダイス:"+str(diece)))
                case 4:
                    pl_inpo.append(["科学者",2,diece])
                    page.add(ft.Text(i+":科学者/"+"死ぬダイス:"+str(diece)))
                case 5:
                    pl_inpo.append(["呪術師",6,diece])
                    page.add(ft.Text(i+":呪術師/"+"死ぬダイス:"+str(diece)))
                case 6:
                    pl_inpo.append(["無職",5,diece])
                    page.add(ft.Text(i+":無職/"+"死ぬダイス:"+str(diece)))
            
            
        page.add(ft.Text("本文",size=25))
        page.add(texts)
        page.add(ft.Text("ダイス",size=25))
        page.add(ft.Row([ft.Text("対象:"),dd,before,after,change_button]))
        page.add(ft.Text("ダイスログ",size=20))
        page.add(log)
        page.add(ft.Text(keywords,size=20))

    page.title = "怪談白物語-準備" 
    
    sinarioname=ft.TextField("",hint_text="シナリオ名")
    maintext=ft.TextField("",hint_text="本文")
    new_task = ft.TextField(hint_text="キーワード",data=[],width=470)
    players = ft.TextField(hint_text="プレイヤーの名前を入力(それと空白区切りで死ぬダイスを設定)",data=[],width=470)
    log = ft.ListView(expand=0, spacing=10, padding=20, auto_scroll=True,height=200)
    texts = ft.ListView(expand=0, spacing=10, padding=20, auto_scroll=False,height=300)
    start_ok=ft.TextButton("さあ、ゲームを始めよう!",on_click=start,data=0)
    

    page.add(ft.Text("シナリオの名前を入力"))
    page.add(sinarioname)
    page.add(ft.Text("本文を入力"))
    page.add(maintext)
    page.add(ft.Row([new_task, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked)]))
    page.add(ft.Row([players, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked_player)]))
    page.add(start_ok)

    page.update()
    

   

    
    
    
ft.app(target=main)



