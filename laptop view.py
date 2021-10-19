from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.bottomsheet import MDCustomBottomSheet
import datetime
from datetime import date
from kivy.properties import StringProperty
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
import sqlite3 as sql
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.config import Config
Config.set('graphics', 'resizable', True)
import webbrowser
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
Window.size=(350,600)

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.behaviors import RectangularRippleBehavior, BackgroundColorBehavior, CircularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout
helpstr = '''
ScreenManager:
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import F kivy.factory.Factory
#:import Factory kivy.factory.Factory
    
    
    Student:
    It:
    Btn:
    It1:
    Btn1:
    It2:
    Btn2:
    Seem:
    To:
    Task:
    Todo: 
    Sin:
    Sin2:
    My:
    My2:
#######################################################Mark stor############################################
<Student>:
    name : 'student'
    FloatLayout:
		canvas.before:		
			Rectangle:
				size:self.size
				pos:self.pos
				
		MDFloatLayout:
            pos_hint:{'x':0.050,'y':.010}
            size_hint:.1000,.0
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#0304ff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
		MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:1,.1
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#fbea3b')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
    
    
    MDLabel:
		text:'<=Workers '
		font_size:"30dp"
		pos_hint:{'x':.5,'y':.200}
		color:'#fe0112'
		bold:True
		outline_color:'#FFFF00'  
		outline_width:4    
		
	MDImageButton:
		source:'emp.jpeg'
		font_color:0,0,0,1
		size_hint_y:.2
		size_hint_x:.3
		pos_hint:{'x':.2,'y':.6}
		back_color:(0,0,0,1)
		on_press:
			root.manager.current='it'
			root.manager.transition.direction='up'
	MDImageButton:
		source:'my.png'
		font_color:0,0,0,1
		size_hint_y:.2
		size_hint_x:.3
		pos_hint:{'x':.2,'y':.20}
		back_color:'#fe0112'
		on_press:
			root.manager.current='to'
			root.manager.transition.direction='down'
	MDLabel:
		text:'( OR )'
		font_size:40
		color:'#02ff02'
		bold:True
		pos_hint:{'x':.2,'y':.0}
		outline_color:(0,0,0,1)  
		outline_width:3		
	MDLabel:
		text:'<=My Works'
		font_size:"25dp"
		pos_hint:{'x':.5,'y':-.195}
		color:'#fe0112'
		bold:True
		outline_color:(0,0,0,1)  
		outline_width:5  
	MDIconButton:
        icon:'refresh'
        theme_text_color: "Custom"
        text_color: "#FF0000"
        user_font_size : '30dp'	
        pos_hint:{'x':.6,'y':.9}
		#pos_hint:{'x':.9,'y':.42}
		on_release:
		    root.add_text_inputs3()	
	MDRaisedButton:
        text:'EXIT=>'
        bold:True 
        underline:True
        outline_color:'#000000'
        font_size:"20dp"
        pos_hint: {'center_x':.8,'center_y':.07}
        #on_release:app.stop()
        on_release:app.ext()	
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "My contract..."
                        elevation: 15
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        md_bg_color:app.theme_cls.accent_color
                        
    
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'a.jpg'
                
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Name=Dakshinamoorthi.R'
                            font_size:"10dp"
                            IconLeftWidget:
                                icon: 'human'
                        OneLineIconListItem:
                            text: 'AGE=45'
                            IconLeftWidget:
                                icon: 'face-profile'
                        OneLineIconListItem:
                            text:'NOBILE=9943574279'
                            IconLeftWidget:
                                icon: 'phone'
                        OneLineIconListItem:
                            text:'Work=Calendar '
                            
                            IconLeftWidget:
                                icon: 'tools'        
                        OneLineIconListItem:
                            text:'Location'
                            on_press: app.open2()
                            IconLeftWidget:
                                icon: 'google-maps'
                                        
                BoxLayout:
                    orientation: 'vertical'
                    spacing: '8dp'
                    padding: '8dp'
                    Image:
                        source:'am.jpg'   
                                                 
			    ScrollView:
                    MDList:
                        OneLineIconListItem:
                        
                            text: 'Name=Karbhaka Lakshmi t'
                            #font_size:"20dp"
                            
                            IconLeftWidget:
                                icon: 'human'
                        OneLineIconListItem:
                            text: 'AGE=35'
                            IconLeftWidget:
                                icon: 'face-profile'
                        OneLineIconListItem:
                            text:'NOBILE=9655097290'
                            IconLeftWidget:
                                icon: 'phone'
                        OneLineIconListItem:
                            text:'work=Appalam Business'
                            
                            IconLeftWidget:
                                icon: 'tools'        
                        OneLineIconListItem:
                            text:'Location'
                            on_press: app.open1()
                            IconLeftWidget:
                                icon: 'google-maps'
                                    
	#MDLabel:
		#text:'WELCOM GRADUATE...'
		#font_size:45
		#pos_hint:{'x':.2,'y':.445}		
		#bold:True
		#outline_color:'#04ff01' 
		#outline_width:2
	#Label:
	#	text:'________________________'
	#	font_size:65
	#	pos_hint:{'x':.0,'y':.425}
	#	color:'#ff0604'
	#	bold:True
    MDIconButton:
        icon:'eye-off'
        theme_text_color: "Custom"
        text_color: "#008000"
        user_font_size : '35dp'	
        pos_hint:{'x':.8,'y':.9}
		#pos_hint:{'x':.9,'y':.42}
		on_press:
		    root.manager.current='sin2'
		    root.manager.transition.direction='up'
    MDIconButton:
        icon:'eye-off'
        theme_text_color: "Custom"
        text_color: "#FF0000"
        user_font_size : '35dp'	
        pos_hint:{'x':.6,'y':.9}
		#pos_hint:{'x':.9,'y':.42}
		on_press:
		    root.manager.current='sin'
		    root.manager.transition.direction='up'
<It>:
    name: 'it'
    date:date
    container: container
	FloatLayout:
		canvas.before:	
			Rectangle:
				size:self.size
				pos:self.pos
				source:'m1.jpg'
		MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:'1dp','.1dp'
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#FF4500')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
		
	MDLabel:
		text:"Wokers' Details..."
		font_size:"32dp"
		pos_hint:{'x':.2,'y':.445}
		bold:True
		#italic:True
		outline_color:'#fff715' 
		outline_width:2
	Label:
		text:'________________________'
		font_size:"65dp"
		pos_hint:{'x':.0,'y':.425}
		color:'#B0E0E6'
		bold:True
    
        
	MDBoxLayout:
		#orientation:'horizontal'
		MDFloatLayout:
			size_hint:".1dp",".1dp"
			pos_hint:{'x':0,'y':.0}
			
            
            MDLabel:
                id:date
                text:" "
                pos_hint:{'x':.1,'y':.7} 
                #pos_hint: {'center_x':.570,'center_y':.89}
        
                font_size:"15dp"
                bold:True
                color:'#FFFF00'
                outline_color:'#000000' 
		        outline_width:2
		ScrollView:
            size_hint: ".3dp", ".70dp"
			pos_hint:{'x':.4,'y':.12}
            #bar_inactive_color:
            	#get_color_from_hex('00640')
            bar_color:
            	get_color_from_hex('#21b68a')
            effect_cls: "ScrollEffect"
            bar_width:"10dp"
			GridLayout:
				id:container
				cols:1
				height:self.minimum_height
				row_default_height:"320dp"
				size_hint_y:None
    MDFloatingActionButton:
        icon:"tools"
        #icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#FFFF00"
        user_font_size : '35dp'
	    pos_hint:{'x':.07,'y':.63}
		on_release:
			#Factory.custompopup().open()
		    root.manager.current="seem"
	MDLabel:
	    text:'  Workers'
	    color:"#FF4500"
	    bold:True
	    underline:True
	    pos_hint:{'x':.0,'y':.1}	    
		font_size:"19dp"		
	MDFloatingActionButton:
        icon:'refresh'
        theme_text_color: "Custom"
        #text_color: "#ffff00"
        
        user_font_size : '37dp'	
		pos_hint:{'x':.07,'y':.44}
		on_release:
			root.add_text_inputs()
	MDLabel:
	    text:'Show data'
	    color:"#FF4500"
	    underline:True
	    bold:True
	    pos_hint:{'x':.0,'y':-.1}	    
		font_size:"18dp"		
	
	MDFloatingActionButton:
        icon: 'home'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#FFFF00"
        pos_hint: {'x':.07,'y':.22}
        user_font_size : '35dp'
        on_press:
            root.manager.current = 'student'
            root.manager.transition.direction = 'right'
#<custompopup@Popup>:
<Seem>:
    name:'seem'
	ugsem:ugsem
	ugexam:ugexam
	ugsub1:ugsub1
	ugsub2:ugsub2
	ugsub3:ugsub3
	ugsub4:ugsub4
	ugsub5:ugsub5
	ugsub6:ugsub6
	ugtotal:ugtotal
	ugsub10:ugsub10
	ugsub11:ugsub11
	ugsub12:ugsub12
	date:date
	size_hint:".9dp",".9dp"
	separator_height: 0
	background_color:0,0,0,0.4
	border: (1, 1, 1, 1)
	MDFloatLayout:
	     
		#canvas.before:
		#	Color:
		#		rgba:get_color_from_hex('#ffffff')
		#	Rectangle:
		#		size:self.size
		#		pos:self.pos
		#MDFloatLayout:
         #   pos_hint:{'x':.0,'y':.9}          
          #  size_hint:"1dp",".1dp"
           # canvas.before:
            #    Color:
             #       rgba:get_color_from_hex('#0102ff')
              #  RoundedRectangle:
               #     size:self.size
               #     pos:self.pos
                #    radius:[0,]
		#MDImageButton:
		#	source:'student1.png'
		#	size_hint_y:.35
		#	size_hint_x:.35
		#	pos_hint:{'x':.3,'y':.7}
		MDBoxLayout:
		    text:"enter deatles"
			pos_hint:{'x':.1,'y':.1}          
         #   size_hint:"1dp",".71dp"
            #title:'seeni'
		#	orientation:'horizontal'
		#	color:'#0102ff'
			ScrollView:
				bar_width:'7dp'
				#size_hint: (.10, .73)
				bar_color:
            	    get_color_from_hex('#ff0000')
				GridLayout:
				    
					cols:1
					height:self.minimum_height
					row_default_height:60
					size_hint_y:None
					MDIconButton:
                        icon:'chevron-left'
                        user_font_size:'40dp'
                        pos_hint: {'center_y':.88}
                        theme_text_color:"Custom"
                        text_color:'#0000FF'
                        on_release:
                            root.manager.current='it'
                            root.manager.transition.direction ="right"
					MDLabel:
                        id:date
                        text:" "
                        #pos_hint:{'x':.1,'y':.7} 
                        #pos_hint: {'center_x':.570,'center_y':.89}
                        pos_hint:{'x':.05,'y':.68}
                        font_size:"20dp"
                        bold:True
                        color:'#FFFF00'
                        outline_color:'#000000' 
		                outline_width:2
					MDLabel:
						text:'Date and Week'
						font_size:"35dp"
						halign: 'center'
						#color:0,0,0,1
						text_size:self.size
						underline:True
						underline_color:'#020101'
						color:get_color_from_hex('#ff0206')
					MDLabel:
						text:'date-(week)'
						halign: 'center'
						color:0,0,0,1
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugsem
						hint_text: '1/01/2022(sunday)'
						font_size:"19dp"
						multiline:False
						size_hint: "0.6dp","0.1dp"
						mode: "rectangle"
						helper_text_mode: 'on_error'
						icon_right: 'calendar'
					    required : True
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"19dp"
					MDLabel:
					MDLabel:
						text:'Workers name'
						font_size:"33dp"
						halign: 'center'
						#color:0,0,0,1
						text_size:self.size
						underline:True
						underline_color:'#030000'
						color:get_color_from_hex('#ff0206')
					MDLabel:
						text:'NAME 1'
						bold:True
						halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugexam
						hint_text: 'NAME--Counting--Amount'
						multiline:False
						size_hint: "0.7dp","0.1dp"
						icon_right: 'cash-100'
						#required : True
						color:'#fe0200'
					    mode: "rectangle"
						color:0,0,0,1
						#size_hint:"1dp",".35dp"
						#helper_text_mode: 'on_error'
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"
					
					MDLabel:
						text:'NAME 2'
						bold:True
						halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugsub1
						hint_text: 'NAME--Counting--Amount'
						size_hint: "0.7dp","0.1dp"
						mode: "rectangle"
						icon_right: 'cash-100'
						#required : True
						#helper_text_mode: 'on_error'
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"
					MDLabel:
					    text:'NAME 3'
					    bold:True
					    halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugsub2
						hint_text: 'NAME--Counting--Amount'
						size_hint: "0.7dp","0.1dp"
						#helper_text_mode: 'on_error'
						#required : True
                        icon_right: 'cash-100'
                        mode: "rectangle"
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"
					MDLabel:
					    text:'NAME 4'
					    bold:True
					    halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugsub3
						hint_text: 'NAME--Counting--Amount'
						size_hint: "0.7dp","0.1dp"
						#helper_text_mode: 'on_error'
						#required : True
                        icon_right: 'cash-100'
                        mode: "rectangle"
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"
					MDLabel:
					    text:'NAME 5'
					    halign: 'center'
					    bold:True
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugsub4
						hint_text: 'NAME--Counting--Amount'
						size_hint: "0.7dp","0.1dp"
						#helper_text_mode: 'on_error'
                        icon_right: 'cash-100'
                        #required : True
                        mode: "rectangle"
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"
					MDLabel:
					    text:'NAME 6'
					    halign: 'center'
					    bold:True
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugsub5
						hint_text: 'NAME--Counting--Amount'
						size_hint: "0.7dp","0.1dp"
						#helper_text_mode: 'on_error'
						#required : True
                        icon_right: 'cash-100'
                        #icon_right: 'book-open-variant'
                        mode: "rectangle"
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"
					MDLabel:
					    text:'NAME 7'
					    halign: 'center'
					    bold:True
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugsub6
						hint_text: 'NAME--Counting--Amount'
						size_hint: "0.7dp","0.1dp"
						#helper_text_mode: 'on_error'
                        icon_right: 'cash-100'
                        mode: "rectangle"
						#halign: 'center'
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"
					
					MDLabel:
						text:'NAME 8'
						bold:True
						halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugtotal
						hint_text: 'NAME--Counting--Amount'
						size_hint: "0.7dp","0.1dp"
						#helper_text_mode: 'on_error'
                        icon_right: 'cash-100'
                        mode: "rectangle"
						#halign: 'center'
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"
					MDLabel:
					    text:'NAME 9'
					    bold:True
					    halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugsub10
						hint_text: 'NAME--Counting--Amount'
						size_hint: "0.7dp","0.1dp"
						#helper_text_mode: 'on_error'
                        icon_right: 'cash-100'
                        mode: "rectangle"
						#halign: 'center'
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"
					MDLabel:
					    text:'NAME 10'
					    bold:True
					    halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugsub11
						hint_text: 'NAME--Counting--Amount'
						size_hint: "0.7dp","0.1dp"
						#helper_text_mode: 'on_error'
                        icon_right: 'cash-100'
                        mode: "rectangle"
						#halign: 'center'
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"
					
					MDLabel:	
					MDLabel:
						text:'Total counting'
						font_size:"35dp"
						halign: 'center'
						#color:0,0,0,1
						text_size:self.size
						underline:True
						color:get_color_from_hex('#0040ff')		
					MDLabel:
					    text:'Total counting and amount'
					    halign: 'center'
						color:'#020101'
						pos_hint:{'x':0,'y':.7}
						size_hint:".2dp",".2dp"
					MDTextField:
						id:ugsub12
						#text:"TOTAL="
						hint_text: 'Total counting and amount '
						size_hint: "0.7dp","0.1dp"
						#helper_text_mode: 'on_error'
                        icon_right: 'cash-100'
                        mode: "rectangle"
						#halign: 'center'
						multiline:False
						#color:0,0,0,1
						#size_hint:1,.35
						#size:self.size
						pos_hint:{'x':.05,'y':.68}
						#background_color:0,0,0,0
						font_size:"21dp"			
					MDLabel:
					MDFillRoundFlatButton:
						text:'SAVE DATA'
						font_size:"24dp"
						mode: "rectangle"
						md_bg_color:app.theme_cls.primary_color
                        theme_text_color: "Custom"
                        text_color: "#80ff00"
						size_hint:".7dp",".7dp"
						on_press:app.add_user(ugsem.text,ugexam.text,ugsub1.text,ugsub2.text,ugsub3.text,ugsub4.text,ugsub5.text,ugsub6.text,ugtotal.text,ugsub10.text,ugsub11.text,ugsub12.text)
						#background_color:get_color_from_hex('#a4ff12')
						on_release:root.manager.current = 'it'
						   
							
					MDLabel:
					
<Btn>:
    name : 'btn'
    #title:'seeni'
    r1:''
	r2:''
	r3:''
	r4:''
	r5:''
	r6:''
	r7:''
	r8:''
	r9:''
	r10:''
	r11:''
	r12:''
	data:''
	data_id:''
	FloatLayout:
	    
		MDCard:
		    #outline_color:"#ff0000" 
			focus_behavior:True
        	ripple_behavior: True
			#focus_behavior: True
	        orientation: "vertical"  
		
	        padding: "6dp"
	        
	        size_hint: None, None
	        size: "290dp", "300dp"
	        pos_hint: {"center_x": .4, "center_y": .5}
	        MDLabel:       
	        MDLabel:
	            text: root.r1
	            font_size:"20dp"
	            halign: 'center'
	            color:'#fd0104'
	        MDSeparator:
	            height: "1dp"
	            color:'#000200' 
	        MDLabel:
	            text:"WORKERS"
	            color:'#0000CD'
	            underline:True
	            font_size:"22dp"
	            halign: 'center'
	        MDLabel:     
	        MDLabel:           
	            text: root.r2
	            pos_hint:{'x':.2,'y':.2}
	            font_size:"19dp"
	        MDLabel:
	            text: root.r3
	            font_size:"19dp"
	            pos_hint:{'x':.2,'y':.2}
	        MDLabel:    
	            text: root.r4 
	            font_size:"19dp" 
	            pos_hint:{'x':.2,'y':.2}
	        MDLabel:   
	            pos_hint:{'x':.2,'y':.2}
	            text: root.r5
	            font_size:"19dp"
	        MDLabel:    
	            text: root.r6
	            font_size:"19dp"
	            pos_hint:{'x':.2,'y':.2}
	        MDLabel:
	            text: root.r7
	            font_size:"19dp"
	            pos_hint:{'x':.2,'y':.2}
	        MDLabel:
	            text: root.r8   
	            font_size:"19dp" 
	            pos_hint:{'x':.2,'y':.2}   
	        MDLabel:
	            text: root.r9
	            font_size:"19dp"
	            #color:'#ff0000'
	            pos_hint:{'x':.2,'y':.2}
	        MDLabel:
	            text: root.r10
	            pos_hint:{'x':.2,'y':.2}
	            font_size:"19dp"
	        MDLabel:    
	            text: root.r11
	            font_size:"19dp"
	            pos_hint:{'x':.2,'y':.2}    
	        MDSeparator:
	            height: "1dp"
	            color:'#000200'    
	        MDLabel:    
	        MDLabel:
	            text: root.r12
	            font_size:"15dp"
	            color:"#008000"
	            pos_hint:{'x':.2,'y':.2}            
	        
	               
            
	    MDIconButton:
			icon:"delete"
			pos_hint:{'x':.80,'y':.0}
			on_release:root.delete()    								
            on_release:app.opp2()
    
<It1>:
    name: 'it1'
    date:date
    container: container
	FloatLayout:
		canvas.before:	
			Rectangle:
				size:self.size
				pos:self.pos
				source:'fr.jpeg'
		MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:"1dp",".1dp"
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#fb02ca')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
		MDFloatLayout:
            pos_hint:{'x':0.50,'y':.10}
            size_hint:".100dp",".0dp"
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#ffffff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
	MDLabel:
		text:"Fother income..."
		font_size:"35dp"
		pos_hint:{'x':.1,'y':.445}
		color:
		bold:True
		#italic:True
		outline_color:'#FFD700' 
		outline_width:2
	Label:
		text:'________________________'
		font_size:"65dp"
		pos_hint:{'x':.0,'y':.425}
		color:0,0,0,1
		bold:True
	MDBoxLayout:
		#orientation:'horizontal'
		MDFloatLayout:
			size_hint:".1dp",".1dp"
			pos_hint:{'x':0,'y':.10}
			
                
			MDLabel:
                id:date
                text:"     "
                pos_hint:{'x':-.0,'y':-.6}
        
                font_size:"25dp"
                bold:True
                color:'#FFFF00'
                outline_color:'#000000' 
		        outline_width:2		
		ScrollView:
            size_hint: ".3dp", ".70dp"
			pos_hint:{'x':.4,'y':.12}
            #bar_inactive_color:
            	#get_color_from_hex('00640')
            bar_color:
            	get_color_from_hex('#21b68a')
            effect_cls: "ScrollEffect"
            bar_width:"10dp"
			GridLayout:
				id:container
				cols:1
				height:self.minimum_height
				row_default_height:285
				size_hint_y:None
    #MDFloatingActionButton:
    MDIconButton:
        icon:"fee.png"
        #icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#FFFF00"
        user_font_size : '35dp'
	    pos_hint:{'x':.07,'y':.63}
	    on_release:
		    root.manager.current="my"
		on_release:
		    root.manager.current="it1"
	MDLabel:
	    text:'  Add data'
	    bold:True
	    underline:True
	    pos_hint:{'x':.0,'y':.1}	    
		font_size:"19dp"		
	MDFloatingActionButton:
        icon:'refresh'
        theme_text_color: "Custom"
        #text_color: "#ffff00"
        user_font_size : '37dp'	
		pos_hint:{'x':.07,'y':.44}
		on_release:
			root.add_text_inputs1()
	MDLabel:
	    text:'Show data'
	    underline:True
	    bold:True
	    pos_hint:{'x':.0,'y':-.1}	    
		font_size:"19dp"		
	
	MDFloatingActionButton:
        icon: 'home'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#FFFF00"
        pos_hint: {'x':.07,'y':.22}
        user_font_size : '35dp'
        on_press:
            root.manager.current = 'student'
            root.manager.transition.direction = 'right'
    

<Btn1>:
    name : 'btn1'
    a1:''
	a2:''
	a3:''
    a4:''
	data:''
	data_id:''
	FloatLayout:
		MDCard:
		    id:a1
			focus_behavior:True
        	ripple_behavior: True
			#focus_behavior: True
	        orientation: "vertical"
	        padding: "6dp"
	        size_hint: None, None
	        size: "250dp", "250dp"
	        pos_hint: {"center_x": .5, "center_y": .5}
	        MDLabel:
	            text: root.a1
	            font_size:"20dp"
	            color:'#FF1493'
	            halign: 'center'
	            font_size:"20dp"
	          
	        MDSeparator:
	            height: "2dp"
	            halign: 'center'
	        MDLabel:
	            text:"Total celery"
	            font_size:"21dp"
	            underline:True
	            bold:True
	            halign: 'center'                
			MDLabel:
	            text: root.a2
	            font_size:"19dp"
	            pos_hint:{'x':.1,'y':.2}
	            
	         
	        MDLabel:
	            text:"Given the celery"
	            bold:True
	            color:"#0000CD"
	            font_size:"21dp"
	            underline:True
	            halign: 'center'    
	        MDLabel:
	            text: root.a3
	            font_size:"19dp"
	            pos_hint:{'x':.1,'y':.2}
	        MDLabel:
	            text:"My Profit"
	            color:"#32CD32"
	            font_size:"21dp"
	            underline:True
	            bold:True
	            halign: 'center'    
	        MDLabel:
	            text: root.a4
	            font_size:"19dp"
	            pos_hint:{'x':.1,'y':.2}
	              
	                
        MDIconButton:
			icon:"delete"
			pos_hint:{'x':.83,'y':.05}
			on_release:root.delete()
            on_release:app.opp2()
<It2>:
    name: 'it2'
    date:date
    container: container
	FloatLayout:
		canvas.before:	
			Rectangle:
				size:self.size
				pos:self.pos
				source:'fr.jpeg'
		MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:"1dp",".1dp"
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#FFFF00')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
		MDFloatLayout:
            pos_hint:{'x':0.50,'y':.10}
            size_hint:".100dp",".0dp"
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#ffffff')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[30,]
	MDLabel:
		text:"Mother income..."
		font_size:"35dp"
		pos_hint:{'x':.1,'y':.445}
		color:
		bold:True
		#italic:True
		outline_color:'#FF0000' 
		outline_width:2
	Label:
		text:'________________________'
		font_size:"65dp"
		pos_hint:{'x':.0,'y':.425}
		color:0,0,0,1
		bold:True
	MDBoxLayout:
		#orientation:'horizontal'
		MDFloatLayout:
			size_hint:".1dp",".1dp"
			pos_hint:{'x':0,'y':.10}
			
                
			MDLabel:
                id:date
                text:"     "
                pos_hint:{'x':-.0,'y':-.6}
        
                font_size:"25dp"
                bold:True
                color:'#FFFF00'
                outline_color:'#000000' 
		        outline_width:2		
		ScrollView:
            size_hint: ".3dp", ".70dp"
			pos_hint:{'x':.4,'y':.12}
            #bar_inactive_color:
            	#get_color_from_hex('00640')
            bar_color:
            	get_color_from_hex('#21b68a')
            effect_cls: "ScrollEffect"
            bar_width:"10dp"
			GridLayout:
				id:container
				cols:1
				height:self.minimum_height
				row_default_height:285
				size_hint_y:None
    #MDFloatingActionButton:
    MDIconButton:
        icon:"fee.png"
        #icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#FFFF00"
        user_font_size : '35dp'
	    pos_hint:{'x':.07,'y':.63}
	    on_release:
		    root.manager.current="my2"
		on_release:
		    root.manager.current="it2"
	MDLabel:
	    text:'  Add data'
	    bold:True
	    underline:True
	    pos_hint:{'x':.0,'y':.1}	    
		font_size:"19dp"		
	MDFloatingActionButton:
        icon:'refresh'
        theme_text_color: "Custom"
        #text_color: "#ffff00"
        user_font_size : '37dp'	
		pos_hint:{'x':.07,'y':.44}
		on_release:
			root.add_text_inputs2()
	MDLabel:
	    text:'Show data'
	    underline:True
	    bold:True
	    pos_hint:{'x':.0,'y':-.1}	    
		font_size:"19dp"		
	
	MDFloatingActionButton:
        icon: 'home'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#FFFF00"
        pos_hint: {'x':.07,'y':.22}
        user_font_size : '35dp'
        on_press:
            root.manager.current = 'student'
            root.manager.transition.direction = 'right'
    

<Btn2>:
    name : 'btn2'
    b1:''
	b2:''
	b3:''
    b4:''
	data:''
	data_id:''
	FloatLayout:
		MDCard:
		    id:a1
			focus_behavior:True
        	ripple_behavior: True
			#focus_behavior: True
	        orientation: "vertical"
	        padding: "6dp"
	        size_hint: None, None
	        size: "250dp", "250dp"
	        pos_hint: {"center_x": .5, "center_y": .5}
	        MDLabel:
	            text: root.b1
	            font_size:"20dp"
	            color:'#FF1493'
	            halign: 'center'
	            font_size:"20dp"
	          
	        MDSeparator:
	            height: "2dp"
	            halign: 'center'
	        MDLabel:
	            text:"Total celery"
	            font_size:"21dp"
	            underline:True
	            bold:True
	            halign: 'center'                
			MDLabel:
	            text: root.b2
	            font_size:"19dp"
	            pos_hint:{'x':.1,'y':.2}
	            
	         
	        MDLabel:
	            text:"Given the celery"
	            bold:True
	            color:"#0000CD"
	            font_size:"21dp"
	            underline:True
	            halign: 'center'    
	        MDLabel:
	            text: root.b3
	            font_size:"19dp"
	            pos_hint:{'x':.1,'y':.2}
	        MDLabel:
	            text:"My Profit"
	            color:"#32CD32"
	            font_size:"21dp"
	            underline:True
	            bold:True
	            halign: 'center'    
	        MDLabel:
	            text: root.b4
	            font_size:"19dp"
	            pos_hint:{'x':.1,'y':.2}
	              
	                
        MDIconButton:
			icon:"delete"
			pos_hint:{'x':.83,'y':.05}
			on_release:root.deleteo()
            on_release:app.opp2()

    
<To>:
    name: 'to'
    date:date
    container: container
	FloatLayout:
		canvas.before:	
			Rectangle:
				size:self.size
				pos:self.pos
				source:'m2.jpeg'
		MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:'1dp','.1dp'
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#FF4500')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
		
	
    
        
	MDBoxLayout:
		#orientation:'horizontal'
		MDFloatLayout:
			size_hint:".1dp",".1dp"
			pos_hint:{'x':0,'y':.0}
			
            
            MDLabel:
                id:date
                text:" "
                pos_hint:{'x':.1,'y':.7} 
                #pos_hint: {'center_x':.570,'center_y':.89}
        
                font_size:"15dp"
                bold:True
                color:'#FFFF00'
                outline_color:'#000000' 
		        outline_width:2
		ScrollView:
            size_hint: ".5dp", ".69dp"
			pos_hint:{'x':.4,'y':.15}
            #bar_inactive_color:
            	#get_color_from_hex('00640')
            bar_color:
            	get_color_from_hex('#21b68a')
            effect_cls: "ScrollEffect"
            bar_width:"6dp"
			GridLayout:
				id:container
				cols:1
				height:self.minimum_height
				row_default_height:"235dp"
				size_hint_y:None
	    	
		
    MDLabel:
		text:'Other details..'
		font_size:"34dp"
		pos_hint:{'x':.2,'y':.445}
		bold:True
		#italic:True
		outline_color:'#fff715' 
		outline_width:2
	Label:
		text:'________________________'
		font_size:"60dp"
		pos_hint:{'x':.0,'y':.425}
		color:'#0e0100'
		bold:True
    MDLabel:
        id:date
        text:""
        pos_hint:{'x':.0,'y':.3}
        #font_name:"Poppins-SemiBold.ttf"
        font_size:'17dp'
        color:'#FF1493'
        underline:True
        bold:True
    MDFloatingActionButton:
        icon:'account-plus'
        md_bg_color:app.theme_cls.primary_color
        theme_text_color: "Custom"
        text_color: "#020700"
        user_font_size : '27dp'
        pos_hint:{'x':.02,'y':.02}
	    #pos_hint:{'x':.07,'y':.63}
	    on_release:
		    root.manager.current ='todo'
		    root.manager.transition.direction = 'left'
	
	MDFloatingActionButton:
        icon:'refresh'
        theme_text_color: "Custom"
        text_color: "#FF0000"
        user_font_size : '40dp'	
        pos_hint:{'x':.4,'y':.02}
		#pos_hint:{'x':.07,'y':.42}
		on_release:
			root.add_text_inputs3()
	MDFloatingActionButton:
	    #icon:'chevron-left'
        icon:'home'
        theme_text_color: "Custom"
        text_color: "#020700"
        user_font_size : '27dp'	
		pos_hint:{'x':.810,'y':.02}
		on_release:
			root.manager.current = 'student'
            root.manager.transition.direction = 'right'		
				
	
		
<Todo>:
    name:'todo' 
    date:date
    FloatLayout:
        
        canvas.before:
            Color:
                rgba: rgba("#C0C0C0")
            Rectangle:
                size: self.size
                pos: self.pos        
        MDLabel:
            text:'Date and Week'
            bold:True
            underline:True
            pos_hint: {'center_x':.6,'center_y':.83}
            font_size:'35dp'
        MDLabel:
            id:date
            bold:True
            color:"#FF1493"
            text:""
            pos_hint: {'center_x':.570,'center_y':.89}
            #font_name:"Poppins-SemiBold.ttf"
            font_size:'18dp'    
            
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.74}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            TextInput:
                id: title
                hint_text:'Date and Week'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
        MDLabel:
            text:'My contract details...'
            bold:True
            underline:True
            pos_hint: {'center_x':.6,'center_y':.60}
            font_size:"30dp"        
            color:'#FF0000'
        MDFloatLayout:
            size_hint:".85dp",".30dp"
            pos_hint: {'center_x':.5,'center_y':.40}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            TextInput:
                id:task
                hint_text:'MY Contract...'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:"190dp"
                cursor_width:'2dp'
                foreground_color:(0,0,0)
                background_color:0,0,0,0
                
                padding:17
                font_size:'25dp'
        Button:
            text:'Save MY Task!'
            ripple_behavior: True
            size_hint:".50dp" ,".08dp"
            pos_hint: {'center_x':.5,'center_y':.17}
            background_color:0,0,0,0
            font_size:'25dp'
            color:'#000000'
            
            on_press:app.add_user3(title.text,task.text)
            on_release:
                root.manager.current ='to'
                             
            canvas.before:
                Color:
                    rgb:(127/255,255/255,0)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            
        MDIconButton:
            icon:'chevron-left'
            user_font_size:'40dp'
            pos_hint: {'center_x':0.1,'center_y':0.1}
            #pos_hint: {'center_y':.95}
            theme_text_color:"Custom"
            text_color:'#FF0000'
            on_release:
                root.manager.current='to'
                root.manager.transition.direction = 'right'
       
<Sin>:
    name:'sin'
    date:date
    FloatLayout:
        
        canvas.before:
            Color:
                rgba: rgba("#FF0000")
            Rectangle:
                size: self.size
                pos: self.pos 
        MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:"1dp",".1dp"
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#FFFF00')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]
                       
        MDLabel:
            text:'Fother business details...'
            bold:True
            color:"#FF4500"
            underline:True
            pos_hint: {'center_x':.6,'center_y':.94}
            font_size:'29dp'
            outline_color:'#000000' 
		    outline_width:2
		Label:
		    text:'________________________'
		    font_size:"50dp"
		    pos_hint:{'x':.0,'y':.425}
		    color:0,0,0,1
		    bold:True    
        MDLabel:
            id:date
            bold:True
            color:"#FF1493"
            text:""
            pos_hint: {'center_x':.570,'center_y':.89}
            #font_name:"Poppins-SemiBold.ttf"
            font_size:'18dp'
            outline_color:'#FF0000' 
		    outline_width:1    
            
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.60}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            TextInput:
                id:login
                hint_text:'Enter your password'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#000000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
       
        Button:
            text:'login'
            ripple_behavior: True
            size_hint:".50dp" ,".08dp"
            pos_hint: {'center_x':.5,'center_y':.36}
            background_color:0,0,0,0
            font_size:'25dp'
            color:'#000000'
            on_release:
                root.manager.current ='it1'if login.text=="tk" else'sin'
                             
            canvas.before:
                Color:
                    rgb:(127/255,255/255,0)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            
        MDIconButton:
            icon:'chevron-left'
            user_font_size:'50dp'
            pos_hint: {'center_x':0.1,'center_y':0.2}
            #pos_hint: {'center_y':.95}
            theme_text_color:"Custom"
            text_color:'#FFFF00'
            on_release:
                root.manager.current='student'
                root.manager.transition.direction = 'right'

<Sin2>:
    name:'sin2'
    date:date
    FloatLayout:
        
        canvas.before:
            Color:
                rgba: rgba("#008000")
            Rectangle:
                size: self.size
                pos: self.pos  
        MDFloatLayout:
            pos_hint:{'x':.0,'y':.9}          
            size_hint:"1dp",".1dp"
            canvas.before:
                Color:
                    rgba:get_color_from_hex('#FFFF00')
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[0,]              
        MDLabel:
            text:'Mother business details...'
            bold:True
            color:"#FF4500"
            underline:True
            pos_hint: {'center_x':.5,'center_y':.94}
            font_size:'29dp'
            outline_color:'#000000' 
		    outline_width:2
		Label:
		    text:'________________________'
		    font_size:"50dp"
		    pos_hint:{'x':.0,'y':.425}
		    color:0,0,0,1
		    bold:True    
        MDLabel:
            id:date
            bold:True
            color:"#FF1493"
            text:""
            pos_hint: {'center_x':.570,'center_y':.89}
            #font_name:"Poppins-SemiBold.ttf"
            font_size:'18dp'    
            
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.60}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            TextInput:
                id:login
                hint_text:'Enter your password'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
       
        Button:
            text:'login'
            ripple_behavior: True
            size_hint:".50dp" ,".08dp"
            pos_hint: {'center_x':.5,'center_y':.36}
            background_color:0,0,0,0
            font_size:'25dp'
            color:'#FF0000'
            on_release:
                root.manager.current ='it2'if login.text=="tk" else'sin2'
                             
            canvas.before:
                Color:
                    rgb:(127/255,255/255,0)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            
        MDIconButton:
            icon:'chevron-left'
            user_font_size:'50dp'
            pos_hint: {'center_x':0.1,'center_y':0.2}
            #pos_hint: {'center_y':.95}
            theme_text_color:"Custom"
            text_color:'#FFFF00'
            on_release:
                root.manager.current='student'
                root.manager.transition.direction = 'right'

<My2>:
    name:"my2"    
    date:date
    FloatLayout:
        
        canvas.before:
            Color:
                rgba: rgba("#C0C0C0")
            Rectangle:
                size: self.size
                pos: self.pos        
        MDLabel:
            text:'Date and Week'
            bold:True
            underline:True
            pos_hint: {'center_x':.8,'center_y':.85}
            font_size:'25dp'
        MDLabel:
            id:date
            bold:True
            color:"#FFFF00"
            text:""
            pos_hint: {'center_x':.579,'center_y':.92}
            #font_name:"Poppins-SemiBold.ttf"
            font_size:'20dp'    
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.78}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            #MDTextField:
            TextInput:
                id: pgsem1
                hint_text:'Date and Week'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
        MDLabel:
            text:'Investment'
            color:"#FF4500"
            pos_hint: {'center_x':.8,'center_y':.70}
            bold:True
            #pos_hint: {'center_x':.6,'center_y':.79}
            font_size:'25dp'
                    
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.63}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            #MDTextField:
            TextInput:
                id: pgexam1
                hint_text:'Investment'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
        MDLabel:
            text:'Sales items'
            pos_hint: {'center_x':.8,'center_y':.55}
            bold:True
            color:"#FF4500"
            #pos_hint: {'center_x':.6,'center_y':.79}
            font_size:'25dp'        
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.48}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            #MDTextField:
            TextInput:
                id: pgsub11
                hint_text:'Sales items'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
        MDLabel:
            text:'My Profit'
            color:"#FF4500"
            pos_hint: {'center_x':.8,'center_y':.41}
            bold:True
            #pos_hint: {'center_x':.6,'center_y':.79}
            font_size:'25dp'                            
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.33}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            #MDTextField:
            TextInput:
                id: pgsub21
                hint_text:'My Profit'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
        
        
        Button:
            text:'Save Data'
            ripple_behavior: True
            size_hint:".50dp" ,".08dp"
            pos_hint: {'center_x':.5,'center_y':.17}
            background_color:0,0,0,0
            font_size:'25dp'
            color:'#0000CD'
            
            on_press:app.add1(pgsem1.text,pgexam1.text,pgsub11.text,pgsub21.text)
            on_release:
                root.manager.current ='it2'
                             
            canvas.before:
                Color:
                    rgb:(127/255,255/255,0)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            
        MDIconButton:
            icon:'chevron-left'
            user_font_size:'40dp'
            pos_hint: {'center_x':0.1,'center_y':0.1}
            #pos_hint: {'center_y':.95}
            theme_text_color:"Custom"
            text_color:'#FF0000'
            on_release:
                root.manager.current='it2'
                root.manager.transition.direction = 'right'
<My>:
    name:"my"    
    date:date
    FloatLayout:
        
        canvas.before:
            Color:
                rgba: rgba("#C0C0C0")
            Rectangle:
                size: self.size
                pos: self.pos        
        MDLabel:
            text:'Date and Week'
            bold:True
            underline:True
            pos_hint: {'center_x':.8,'center_y':.85}
            font_size:'25dp'
        MDLabel:
            id:date
            bold:True
            color:"#FF0000"
            text:""
            pos_hint: {'center_x':.579,'center_y':.92}
            #font_name:"Poppins-SemiBold.ttf"
            font_size:'20dp'    
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.78}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            #MDTextField:
            TextInput:
                id: pgsem
                hint_text:'Date and Week'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
        MDLabel:
            text:'Total celery'
            pos_hint: {'center_x':.8,'center_y':.70}
            bold:True
            #pos_hint: {'center_x':.6,'center_y':.79}
            font_size:'25dp'
                    
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.63}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            #MDTextField:
            TextInput:
                id: pgexam
                hint_text:'My Total celery'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
        MDLabel:
            text:'Given the celery'
            pos_hint: {'center_x':.8,'center_y':.55}
            bold:True
            #pos_hint: {'center_x':.6,'center_y':.79}
            font_size:'25dp'        
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.48}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            #MDTextField:
            TextInput:
                id: pgsub1
                hint_text:'Given the celery'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
        MDLabel:
            text:'My Profit'
            pos_hint: {'center_x':.8,'center_y':.41}
            bold:True
            #pos_hint: {'center_x':.6,'center_y':.79}
            font_size:'25dp'                            
        MDFloatLayout:
            size_hint:".85dp",".08dp"
            pos_hint: {'center_x':.5,'center_y':.33}
            canvas:
                Color:
                    rgb:(238/255,238/255,238/255,1)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            #MDTextField:
            TextInput:
                id: pgsub2
                hint_text:'My Profit'
                size_hint:1,None
                pos_hint: {'center_x':.5,'center_y':.5}
                height:self.minimum_height
                cursor_width:'2dp'
                foreground_color:'#FF0000'
                background_color:0,0,0,0
                padding:"25dp"
                font_size:"18dp"
        
        
        Button:
            text:'Save Data'
            ripple_behavior: True
            size_hint:".50dp" ,".08dp"
            pos_hint: {'center_x':.5,'center_y':.17}
            background_color:0,0,0,0
            font_size:'25dp'
            color:'#0000CD'
            
            on_press:app.add(pgsem.text,pgexam.text,pgsub1.text,pgsub2.text)
            on_release:
                root.manager.current ='it1'
                             
            canvas.before:
                Color:
                    rgb:(127/255,255/255,0)
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    radius:[25]
            
        MDIconButton:
            icon:'chevron-left'
            user_font_size:'40dp'
            pos_hint: {'center_x':0.1,'center_y':0.1}
            #pos_hint: {'center_y':.95}
            theme_text_color:"Custom"
            text_color:'#FF0000'
            on_release:
                root.manager.current='it1'
                root.manager.transition.direction = 'right'
        
	            
<Task>:
    name : 'task'
    #title:'seeni'
    title:''
	task:''
	data:''
	data_id:''
	FloatLayout:
	    
        
		MDCard:
		    id:f
	        orientation: "vertical"  
		
	        padding: "6dp"
	        
	        size_hint: None, None
	        size: "500dp", "200dp"
	        pos_hint: {"center_x": .1, "center_y": .5}
	               
	        MDLabel:
	            id:v
	            text: root.title
	            font_size:"20dp"
	            bold:True
	            pos_hint: {'center_x':.99,'center_y':.6}
	            #halign: 'center'
	            color:'#fd0104'
	            outline_color:'#040204'
            	underline:True
	            
	                  
			MDLabel:
			    id:a
	            text: root.task
	            font_size:"17dp"
	            color:'#000000'
	            #halign: 'center'
	            pos_hint:{'x':.45,'y':.0}
	        MDLabel:
                id:da
                text:""
                font_size:'15dp'
                pos_hint:{'x':.2,'y':.2}    
	        
	    MDIconButton:
			icon:"delete"
			pos_hint:{'x':.8,'y':.7}
			on_release:root.delete3()
			on_release:app.opp2() 
			   								
              
        
            
'''
class Student(Screen):
    pass
sm = ScreenManager()
sm.add_widget(Student(name='student'))
class Btn(Screen):
    pass

    def __init__(self, **kwargs):
        super(Btn, self).__init__(**kwargs)

    def delete(self):
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute('delete from ugstudent where ID=' + self.data_id)
        con.commit()
        con.close()


class It(Screen):
    # self.data_id=data_id
    text = StringProperty()
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(It, self).__init__(**kwargs)

    def add_text_inputs(self):
        self.container.clear_widgets()
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute("""SELECT *FROM ugstudent""")
        row = cur.fetchall()
        for i in row:
            wid = Btn()

            r1 = str(i[1]) + '\n'
            r2 = str(i[2]) + '\n'
            r3 = str(i[3]) + '\n'
            r4 = str(i[4]) + '\n'
            r5 = str(i[5]) + '\n'
            r6 = str(i[6]) + '\n'
            r7 = str(i[7]) + '\n'
            r8 = str(i[8]) + '\n'
            r9 = str(i[9]) + '\n'
            r10 = str(i[10]) + '\n'
            r11 = str(i[11]) + '\n'
            r12 = str(i[12]) + '\n'
            wid.data_id = str(i[0])

            wid.data = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8 + r9 + r10 + r11 + r12

            wid.r1 = r1
            wid.r2 = r2
            wid.r3 = r3
            wid.r4 = r4
            wid.r5 = r5
            wid.r6 = r6
            wid.r7 = r7
            wid.r8 = r8
            wid.r9 = r9
            wid.r10 = r10
            wid.r11 = r11
            wid.r12 = r12

            self.container.add_widget(wid)
class Btn1(Screen):
    pass

    def __init__(self, **kwargs):
        super(Btn1, self).__init__(**kwargs)

    def delete(self):
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute('delete from pgstudent where ID=' + self.data_id)
        con.commit()
        con.close()


class It1(Screen):
    # self.data_id=data_id
    text = StringProperty()
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(It1, self).__init__(**kwargs)

    def add_text_inputs1(self):
        self.container.clear_widgets()
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute("""SELECT *FROM pgstudent""")
        row = cur.fetchall()
        for i in row:
            wid = Btn1()

            a1 = str(i[1]) + '\n'
            a2 = str(i[2]) + '\n'
            a3 = str(i[3]) + '\n'
            a4 = str(i[4]) + '\n'


            wid.data_id = str(i[0])

            wid.data = a1 + a2 + a3 + a4

            wid.a1 = a1
            wid.a2 = a2
            wid.a3 = a3
            wid.a4 = a4


            self.container.add_widget(wid)
class Btn2(Screen):
    pass

    def __init__(self, **kwargs):
        super(Btn2, self).__init__(**kwargs)

    def deleteo(self):
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute('delete from pgstudent2 where ID=' + self.data_id)
        con.commit()
        con.close()


class It2(Screen):
    # self.data_id=data_id
    text = StringProperty()
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(It2, self).__init__(**kwargs)

    def add_text_inputs2(self):
        self.container.clear_widgets()
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute("""SELECT *FROM pgstudent2""")
        row = cur.fetchall()
        for i in row:
            wid = Btn2()

            b1 = str(i[1]) + '\n'
            b2 = str(i[2]) + '\n'
            b3 = str(i[3]) + '\n'
            b4 = str(i[4]) + '\n'


            wid.data_id = str(i[0])

            wid.data = b1 + b2 + b3 + b4

            wid.b1 = b1
            wid.b2 = b2
            wid.b3 = b3
            wid.b4 = b4


            self.container.add_widget(wid)


class ImageButton(ButtonBehavior, Image):
    pass
class MDImageButton(ButtonBehavior, Image):
    pass
class Seem(Screen):
    pass
sm = ScreenManager()


sm.add_widget(It(name='it'))
sm.add_widget(Btn(name="btn"))
sm.add_widget(It1(name='it1'))
sm.add_widget(Btn1(name="btn1"))
sm.add_widget(Seem(name="seem"))
sm.add_widget(It2(name='it2'))
sm.add_widget(Btn2(name="btn2"))
class MY_marks(MDApp):######  main class   ######

    def build(self):
        self.strng = Builder.load_string(helpstr)
        #self.icon='applogo.png'
        return self.strng
    #Window.bind(on_keyboard=self.check_back_btn)
    def check_back_btn(*args):
        if args[1]==27:
            print("Don't press tha back button")
            return True
    def add_user(self, ugsem,ugexam,ugsub1,ugsub2,ugsub3,ugsub4,ugsub5,ugsub6,ugtotal,ugsub10,ugsub11,ugsub12):
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute(
            """ INSERT INTO ugstudent(ugsem,ugexam,ugsub1,ugsub2,ugsub3,ugsub4,ugsub5,ugsub6,ugtotal,ugsub10,ugsub11,ugsub12) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (ugsem,ugexam,ugsub1,ugsub2,ugsub3,ugsub4,ugsub5,ugsub6,ugtotal,ugsub10,ugsub11,ugsub12))
        con.commit()
        con.close()
    def add(self, pgsem,pgexam,pgsub1,pgsub2):
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute(
            """ INSERT INTO pgstudent(pgsem,pgexam,pgsub1,pgsub2) VALUES (?,?,?,?)""",
            (pgsem,pgexam,pgsub1,pgsub2))
        con.commit()
        con.close()
    def add1(self, pgsem1,pgexam1,pgsub11,pgsub21):
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute(
            """ INSERT INTO pgstudent2(pgsem1,pgexam1,pgsub11,pgsub21) VALUES (?,?,?,?)""",
            (pgsem1,pgexam1,pgsub11,pgsub21))
        con.commit()
        con.close()

    def add_user3(self, title, task):
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute(
            """ INSERT INTO studen(title,task) VALUES (?,?)""",
            (title, task))
        con.commit()
        con.close()
    def ext(self):
        self.task1 = MDDialog(title='Are you sure?',type="confirmation",text=f"Are you sure?,EXIT APP!",
                                buttons=[MDRaisedButton(text="NO",on_release=self.ta), MDRaisedButton(text="YES",on_release=self.exte)])
        self.task1.open()
    def ta(self, obj):
        self.task1.dismiss()
    def exte(self, obj):
        self.stop()

    def open1(self):
        webbrowser.open("https://www.google.com/maps/place/293,+Viswanatham,+Sivakasi,+Tamil+Nadu+626123/@9.4465293,77.7975473,736m/data=!3m1!1e3!4m13!1m7!3m6!1s0x0:0x0!2zOcKwMjYnNDcuNSJOIDc3wrA0Nyc1OS4xIkU!3b1!8m2!3d9.4465293!4d77.799736!3m4!1s0x3b06cee6efede20f:0x3ccacbc5c6d55b32!8m2!3d9.4457061!4d77.7987977!5m1!1e4?hl=en")
    def open2(self):
        webbrowser.open("https://www.google.com/maps/place/0%C2%B000'00.0%22N+0%C2%B000'00.0%22E/@-0.0026824,-0.0021887,746m/data=!3m1!1e3!4m2!3m1!1s0x0:0x0?hl=en")

    def on_start(self):

        today=date.today()
        wd = date.weekday(today)
        #days =['manday', 'tuseday','wednesday','thursday','friday','saturday','sunday']
        year =str(datetime.datetime.now().year)
        month=str(datetime.datetime.now().strftime(''))
        day =str(datetime.datetime.now().strftime('%A (%d-%m-%Y)'))
        self.strng.get_screen('it').date.text=f"{day} {month}  "
        #self.strng.get_screen('it1').date.text=f"{day} {month} "
        self.strng.get_screen('todo').date.text=f"{day} {month}  "
        self.strng.get_screen('to').date.text=f"{day} {month}"
        self.strng.get_screen('seem').date.text=f"{day} {month} "
        self.strng.get_screen('my').date.text=f"{day} {month} "
        self.strng.get_screen('my2').date.text=f"{day} {month}"
    def opp2(self):
        delete1 = MDRaisedButton(text='OK', on_release=self.de)
        self.deletes = MDDialog(title='Successfully Delete!',md_bg_color= get_color_from_hex('#FF3D00'),type="confirmation",text=f"Delete Successfully and Refresh Yourself",
                                buttons=[delete1])
        self.deletes.open()
    def de(self, obj):
        self.deletes.dismiss()
class Task(Screen):
    pass

    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)

    def delete3(self):
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute('delete from studen where ID=' + self.data_id)
        con.commit()
        con.close()
class To(Screen):
    # self.data_id=data_id
    text = StringProperty()
    container = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(To, self).__init__(**kwargs)

    def add_text_inputs3(self):
        self.container.clear_widgets()
        con = sql.connect('seenivasan7.db')
        cur = con.cursor()
        cur.execute("""SELECT *FROM studen""")
        row = cur.fetchall()
        for i in row:
            wid = Task()

            title = str(i[1]) + '\n'
            task = str(i[2]) + '\n'


            wid.data_id = str(i[0])

            wid.data = title + task
            wid.title = title
            wid.task = task


            self.container.add_widget(wid)

class Todo(Screen):
    pass
class Sin(Screen):
    pass
class Sin2(Screen):
    pass
class My(Screen):
    pass
class My2(Screen):
    pass
#sm = ScreenManager()

sm.add_widget(To(name='to'))
sm.add_widget(Task(name="task"))
sm.add_widget(Todo(name='todo'))
sm.add_widget(Sin(name='sin'))
sm.add_widget(Sin2(name='sin2'))
sm.add_widget(My(name='my'))
sm.add_widget(My2(name='my2'))

if __name__ == "__main__":
    MY_marks().run()