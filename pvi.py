#!/usr/bin/env python3
# -*- coding: utf-8 -*-
try:
    import svgwrite
except ImportError:
    print(" Prevue Error:")
    print("     svgwrite could not be imported.")
    print("     You probably need to install svgwrite.")
AGgQSJwB_I = '(' + ';' + ';' + ')'        
AIGClZ_ENn = 20
AOplPhlOqb = 12
ARAhaWarMU = 26    
AbCgUqXDkN = 11
AehQIZrBOE = -75       
AlKeXMetaT = 8
AtdaZWdHDu = AehQIZrBOE
AuvYTQfLWr = AlKeXMetaT + 5   
BFdfDKZysm = 10*(AbCgUqXDkN-2) - 4
BKllWLKmUE = "rgb(0,0,0)"    
BcVqZjnKtk = 'normal'
CDxnLgBxVw = ""
CbPsPijBpc = 0        
CiPNTTbEJE = 0         
CprHciKCVV = 4
DAJPZZkehP = 0 
DTzoNeECkt = 0
DUUyNBJTeg = CprHciKCVV * AbCgUqXDkN
def rh_Init_Dwg( Line_cnt, max_line_len, py_file_path, svg_file_path):
    global DTzoNeECkt, DAJPZZkehP, CiPNTTbEJE, CbPsPijBpc
    global BFdfDKZysm
    max_line_len += 1   
    Line_cnt += 1       
    CiPNTTbEJE = DUUyNBJTeg + BFdfDKZysm + (AOplPhlOqb * max_line_len)
    CbPsPijBpc = (ARAhaWarMU * Line_cnt) + AlKeXMetaT + 15
    DTzoNeECkt = svgwrite.Drawing( svg_file_path, size = ( CiPNTTbEJE, CbPsPijBpc))
    rectangle = DTzoNeECkt.rect(insert=(0, 0), size=('100%', '100%'), fill='white')
    DTzoNeECkt.add( rectangle)
    rectangle = DTzoNeECkt.rect( insert=( 40, 0), size = (BFdfDKZysm, CbPsPijBpc), fill='lightgrey')
    DTzoNeECkt.add( rectangle)
    return
DjBjZwVqxP = [[[0,0],[20,0],[20,30],[0,30],],]
DrovcoW_RL = [[[0,0],],]
DuPxNRJkbT = [ [[0,30],[0,7],[5,2],[14,2],[17,5],
        [17,0],[20,0],[20,30],[17,30],[17,21],
        [7,15],[17,9],[13,5],[6,5],[3,8],
        [3,30]],]
DuwutE_IRa = [[[17,30],[17,21],[7,15],[17,9],[17,0],[20,0],[20,30],],]
DzLtRUqYwr = [[[17,30],[17,0],[20,0],[20,30],],]
DzochdSXbt = [[[17,30],[17,20],[8,20],[8,10],[17,10],[17,0],[20,0],[20,30],],]
EAPkD_zEko = [[[17,6],[17,0],[20,0],[20,9],],
       [[17,30],[17,24],[20,21],[20,30],],]
ENdvkWgWnw = [[[0,11],[0,8],[20,8],[20,11] ],
       [[0,22],[0,19],[20,19],[20,22],],]
EOfV_gMZJm = [[[0,11],[0,8],[2,8],[18,19],[20,19],[20,22],[18,22],[2,11],],
       [[0,22],[0,19],[2,19],[7,16],[9,17],[2,22],],
       [[11,13],[18,8],[20,8],[20,11],[18,11],[13,14],],]
EXuxFPpjgH = [[[0,11],[0,8],[14,8],[17,5],[17,0],[20,0],[20,6],[15,11],],
        [[0,22],[0,19],[15,19],[20,24],[20,30],[17,30],[17,25],[14,22],],]
EYZyOBAPXU = [[[0,5],[3,8],[20,8],[20,11],[2,11],[0,9],],
       [[0,21],[2,19],[20,19],[20,22],[3,22],[0,25],],]
EZfPb_zbH_ = [[[0,17],[0,14],[15,14],[17,12],[17,0],[20,0],[20,13],[16,17],],]
EgXUkjtvWL = [[[0,30],[0,0],[3,0],[3,13],[7,19],[3,19],[3,30],],
       [[17,30],[17,0],[20,0],[20,30],],]
EnXzdEwztn = [[[0,17],[0,14],[16,14],[20,18],[20,30],[17,30],[17,19],[15,17],],]
EqYlh_JLKu = [[[0,17],[0,14],[20,14],[20,17],],]
EzmZpXdIV_ = [[[0,30],[0,0],[3,0],[3,9],[8,14],[20,14],[20,17],[7,17],[3,13],[3,30],],
        [[17,13],[17,0],[20,0],[20,13],],
        [[17,30],[17,18],[20,18],[20,30],],]
FOcNQHECHF = [[[0,22],[0,18],[4,14],[20,14],[20,17],[5,17],],]
FXMECaIjlp = [[[17,0],[17,17],[15,19],[15,22],[17,24],[20,24],[20,0],],]
FgUQfBVVlA = [[[0,24],[0,17],[2,19],[2,22],],]
FpTCFZmNFs = [[[4,19],[2,17],[2,14],[4,12],[7,12],[9,14],
        [20,14],[20,17],[9,17],[7,19],],]
FqIVSe_blf = [[[0,21],[0,9],[8,14],[20,14],[20,17],[8,17],],]
FxIxKjavqA = [[[17,13],[17,0],[20,0],  [20,13],],
       [[0,17], [0,14], [20,14],[20,17],],
       [[17,30],[17,18],[20,18],[20,30],],]
def JTzwahteUo( char):
    global AtdaZWdHDu, AuvYTQfLWr, DTzoNeECkt, BKllWLKmUE, BcVqZjnKtk
    DTzoNeECkt.add( DTzoNeECkt.text(
        char,
        insert = ( AtdaZWdHDu + 83, AuvYTQfLWr + 15),    
        text_anchor = "middle",
        dominant_baseline = "hanging",
        font_size = "18px",
        font_family = "DejaVu Sans Mono",
        fill = BKllWLKmUE,
        font_weight = BcVqZjnKtk
        ))
    AtdaZWdHDu += AbCgUqXDkN
    return
def JYXwWdqplD( char, rgb_color):
    global AtdaZWdHDu, AuvYTQfLWr, DTzoNeECkt, BKllWLKmUE
    DTzoNeECkt.add( DTzoNeECkt.text(
        char,
        insert = ( AtdaZWdHDu+4, AuvYTQfLWr+15), 
        text_anchor = "middle",
        dominant_baseline = "hanging",
        font_size = "14px",
        font_family = "Ubuntu Sans Mono Regular",   # was "DejaVu Sans Mono"
        fill = rgb_color,
        font_weight = 'bold'
        ))
    AtdaZWdHDu += (AbCgUqXDkN-2)
    return
def JaTnhZWaeX():
    global AtdaZWdHDu, AuvYTQfLWr
    AtdaZWdHDu = AehQIZrBOE + DUUyNBJTeg  
    AuvYTQfLWr += ARAhaWarMU
    return
def JhkgQZDktM( which_gN, gNstr ):
    global DuPxNRJkbT, CDxnLgBxVw
    global AtdaZWdHDu, AuvYTQfLWr, DTzoNeECkt
    glyph = which_gN
    shifted = []
    for polygon in glyph:  
        shifted += [(px, py) for (px, py) in polygon]
    cell = DTzoNeECkt.polygon( points=shifted)  
    CDxnLgBxVw = gNstr
    DTzoNeECkt.defs.add(cell)
    cell['id'] = CDxnLgBxVw
    return
def JmPWykfOzG( ):
    global DuPxNRJkbT, DzLtRUqYwr, DzochdSXbt, EOfV_gMZJm, EgXUkjtvWL, EqYlh_JLKu, FqIVSe_blf, CDxnLgBxVw
    global AtdaZWdHDu, AuvYTQfLWr, DTzoNeECkt
    JhkgQZDktM(  DuPxNRJkbT, "G3" )
    JhkgQZDktM(  DzLtRUqYwr, "G5" )
    JhkgQZDktM(  DzochdSXbt, "G6" )
    JhkgQZDktM( EgXUkjtvWL, "G13" )
    JhkgQZDktM( EqYlh_JLKu, "G15" )
    JhkgQZDktM( FqIVSe_blf, "G21" )
    return
def JsKHAsKxja( id_str):
    global AtdaZWdHDu, AuvYTQfLWr, DTzoNeECkt
    global CDxnLgBxVw
    CDxnLgBxVw = id_str
    DTzoNeECkt.add(DTzoNeECkt.use('#' + CDxnLgBxVw, insert=(AtdaZWdHDu, AuvYTQfLWr), fill="rgb(80,80,200)"))
    AtdaZWdHDu += AIGClZ_ENn
    return
def KAI_KbejHa( glyph):
    global AtdaZWdHDu, AuvYTQfLWr, DTzoNeECkt
    for polygon in glyph:  
        shifted = [(px + AtdaZWdHDu, py + AuvYTQfLWr) for (px, py) in polygon]
        DTzoNeECkt.add( DTzoNeECkt.polygon( points=shifted, fill="rgb(80,80,200)"))  
        continue
    AtdaZWdHDu += AIGClZ_ENn
    return
def KAoaFayWyE( glyph):
    global AtdaZWdHDu, AuvYTQfLWr, DTzoNeECkt
    for polygon in glyph:  
        shifted = [(px + AtdaZWdHDu, py + AuvYTQfLWr) for (px, py) in polygon]
        DTzoNeECkt.add( DTzoNeECkt.polygon( points=shifted, fill="grey"))
        continue
    AtdaZWdHDu += AIGClZ_ENn
    return
def KJuatGQHkm( ss):
    global BKllWLKmUE, BcVqZjnKtk, AtdaZWdHDu
    if len( ss) >= 4:
        if ss[ -4 : ] == AGgQSJwB_I:      
            ss = '©'+'©'+'D' + ss[ : -4]       
            #end
        #end
    BKllWLKmUE = "rgb(0,0,0)"    
    BcVqZjnKtk = 'normal'      
    JTzwahteUo( ' ')
    color_state = 'B'
    while True:
        while True:
            while len( ss) >= 3:
                if ss[ 0:2] != '©©':
                    break
                ss = ss[ 2:]        
                color_ch = ss[ 0]   
                ss = ss[ 1:]        
                color_state = color_ch
                continue
            if color_state == 'B':
                BKllWLKmUE = "rgb(0,0,0)"      
                BcVqZjnKtk = 'normal'
                break
            if color_state == 'G':
                BKllWLKmUE = "rgb(0,125,0)"    
                BcVqZjnKtk = 'normal'
                break
            if color_state == 'D':
                BKllWLKmUE = "rgb( 90,90,0)"   
                BcVqZjnKtk = 'normal'
                break
            if color_state == 'R':
                BKllWLKmUE = "rgb(150,0,0)"    
                BcVqZjnKtk = 'bold'
                break
            if color_state == 'O':
                BKllWLKmUE = "rgb(190,145,0)"
                BcVqZjnKtk = 'bold'
                #end
            break
        if len( ss) > 0:
            ch = ss[0]
            JTzwahteUo( ch)
            ss = ss[ 1:]      
        else:
            break
        continue
    JaTnhZWaeX()
    return
def KsQdModhzX( word, ss):
    KAoaFayWyE( DjBjZwVqxP)
    for gg in word:
        KAI_KbejHa( gg)
        continue
    KAoaFayWyE( DjBjZwVqxP)
    KJuatGQHkm( ss)
    return
def KurWDlBnwf( gg, ss):
    KAI_KbejHa( gg)
    KJuatGQHkm( ss)
    return
def LHrSNWXTCi():
    JaTnhZWaeX()
    KurWDlBnwf(  DjBjZwVqxP,  "DjBjZwVqxP ")
    JaTnhZWaeX()
    KurWDlBnwf(  DrovcoW_RL,  "DrovcoW_RL ")
    JaTnhZWaeX()
    KurWDlBnwf(  DuPxNRJkbT,  "DuPxNRJkbT ")
    JaTnhZWaeX()
    KurWDlBnwf(  DuwutE_IRa,  "DuwutE_IRa ")
    JaTnhZWaeX()
    KurWDlBnwf(  DzLtRUqYwr,  "DzLtRUqYwr ")
    JaTnhZWaeX()
    KurWDlBnwf(  DzochdSXbt,  "DzochdSXbt ")
    JaTnhZWaeX()
    KurWDlBnwf(  EAPkD_zEko,  "EAPkD_zEko ")
    JaTnhZWaeX()
    KurWDlBnwf(  ENdvkWgWnw,  "ENdvkWgWnw ")
    JaTnhZWaeX()
    KurWDlBnwf(  EOfV_gMZJm,  "EOfV_gMZJm ")
    JaTnhZWaeX()
    KurWDlBnwf( EXuxFPpjgH, "EXuxFPpjgH ")
    JaTnhZWaeX()
    KurWDlBnwf( EYZyOBAPXU, "EYZyOBAPXU ")
    JaTnhZWaeX()
    KurWDlBnwf( EZfPb_zbH_, "EZfPb_zbH_ ")
    JaTnhZWaeX()
    KurWDlBnwf( EgXUkjtvWL, "EgXUkjtvWL ")
    JaTnhZWaeX()
    KurWDlBnwf( EnXzdEwztn, "EnXzdEwztn ")
    JaTnhZWaeX()
    KurWDlBnwf( EqYlh_JLKu, "EqYlh_JLKu ")
    JaTnhZWaeX()
    KurWDlBnwf( EzmZpXdIV_, "EzmZpXdIV_ ")
    JaTnhZWaeX()
    KurWDlBnwf( FOcNQHECHF, "FOcNQHECHF ")
    JaTnhZWaeX()
    KurWDlBnwf( FXMECaIjlp, "FXMECaIjlp ")
    JaTnhZWaeX()
    KurWDlBnwf( FgUQfBVVlA, "FgUQfBVVlA ")
    JaTnhZWaeX()
    KurWDlBnwf( FpTCFZmNFs, "FpTCFZmNFs ")
    JaTnhZWaeX()
    KurWDlBnwf( FqIVSe_blf, "FqIVSe_blf ")
    JaTnhZWaeX()
    KurWDlBnwf( FxIxKjavqA, "FxIxKjavqA ")
    return
GRGxjdxRIm  = [ "G5",   DrovcoW_RL,    DrovcoW_RL]      
GRegnPACsC  = ["G13",   DrovcoW_RL,    DrovcoW_RL]      
GaESbtPljA  = [  FXMECaIjlp,  FgUQfBVVlA,    DrovcoW_RL,  DrovcoW_RL] 
GcjXmqptTa  = [   DuwutE_IRa,'G21', 'G15', EnXzdEwztn] 
GvNwMZjNAf  = [ 'G3','G21', 'G15', EnXzdEwztn] 
GzTgR_wltO  = [ 'G6',   DrovcoW_RL,    DrovcoW_RL,  DrovcoW_RL] 
HGmqRvGTnU  = [   EAPkD_zEko,  EYZyOBAPXU,    EOfV_gMZJm, EXuxFPpjgH] 
HVACIvhVsg  = [  EZfPb_zbH_,   DrovcoW_RL,    DrovcoW_RL,  DrovcoW_RL] 
HYSfDplebQ  = [  FXMECaIjlp,  FgUQfBVVlA,    DrovcoW_RL,  DrovcoW_RL] 
Hcyo_tFgBE = [   DrovcoW_RL,'G15', 'G15', EnXzdEwztn] 
IBXrCwRNSJ = [  EzmZpXdIV_,'G15', 'G15', EZfPb_zbH_] 
ISZzWAjExy = [ "G5",  FOcNQHECHF, 'G15', EZfPb_zbH_] 
ITsRVEVyrw = ["G13",  FOcNQHECHF, 'G15', EZfPb_zbH_] 
IYysKfPOqP = [ "G5",   DrovcoW_RL,    DrovcoW_RL,  DrovcoW_RL] 
ImhwkXUNDm = [   DrovcoW_RL,   DrovcoW_RL,  DrovcoW_RL]        
IoeMXDPhDo = [ "G5",  FOcNQHECHF, EZfPb_zbH_]        
IrwZJaFJTI = [  EzmZpXdIV_,'G15', 'G15']      
IvPSqNTZpN = ['G15','G15', 'G15']      
JAYCJiFfsS = ["G13",  FOcNQHECHF, 'G15']      
JBQ_HVUilm = [  FxIxKjavqA,'G15', 'G15']      
JBjEMlhlYZ = [   DrovcoW_RL,   DrovcoW_RL,  DrovcoW_RL,  DrovcoW_RL]   
JEHBgL_WtR = [   DrovcoW_RL,  FpTCFZmNFs, 'G15', EnXzdEwztn] 
JFShuDAtdaZWdHDuKw = [  "G5"]                  
JToEfnhxar = [ GRGxjdxRIm, GRegnPACsC, GRGxjdxRIm, GcjXmqptTa, GvNwMZjNAf, GzTgR_wltO, HGmqRvGTnU, HVACIvhVsg, HYSfDplebQ, Hcyo_tFgBE, IBXrCwRNSJ, ISZzWAjExy, ITsRVEVyrw, IYysKfPOqP, ImhwkXUNDm, IoeMXDPhDo, IrwZJaFJTI, IvPSqNTZpN, JAYCJiFfsS, JBQ_HVUilm, JBjEMlhlYZ, JEHBgL_WtR, JFShuDAtdaZWdHDuKw]
def LIzqkPZaMD():
    JaTnhZWaeX()
    KsQdModhzX( GRGxjdxRIm,  " GRGxjdxRIm  under_if_short ")     
    JaTnhZWaeX()
    KsQdModhzX( GRegnPACsC,  " GRegnPACsC  under_loop_short ")   
    JaTnhZWaeX()
    KsQdModhzX( GaESbtPljA,  " GaESbtPljA  return_long ")        
    JaTnhZWaeX()
    KsQdModhzX( GcjXmqptTa,  " GcjXmqptTa  if_cond_long ")       
    JaTnhZWaeX()
    KsQdModhzX( GvNwMZjNAf,  " GvNwMZjNAf  loop_cond_long ")     
    JaTnhZWaeX()
    KsQdModhzX( GzTgR_wltO,  " GzTgR_wltO  stmt_long ")          
    JaTnhZWaeX()
    KsQdModhzX( HGmqRvGTnU,  " HGmqRvGTnU  else_long ")          
    JaTnhZWaeX()
    KsQdModhzX( HVACIvhVsg,  " HVACIvhVsg  corner_long ")        
    JaTnhZWaeX()
    KsQdModhzX( HYSfDplebQ,  " HYSfDplebQ  return_2_long ")      
    JaTnhZWaeX()
    KsQdModhzX( Hcyo_tFgBE, " Hcyo_tFgBE def_fcn_long ")       
    JaTnhZWaeX()
    KsQdModhzX( IBXrCwRNSJ, " IBXrCwRNSJ loop_up_long ")       
    JaTnhZWaeX()
    KsQdModhzX( ISZzWAjExy, " ISZzWAjExy if_end_long ")        
    JaTnhZWaeX()
    KsQdModhzX( ITsRVEVyrw, " ITsRVEVyrw loop_out_long ")      
    JaTnhZWaeX()
    KsQdModhzX( IYysKfPOqP, " IYysKfPOqP under_if_long ")      
    JaTnhZWaeX()
    KsQdModhzX( ImhwkXUNDm, " ImhwkXUNDm blank_short ")        
    JaTnhZWaeX()
    KsQdModhzX( IoeMXDPhDo, " IoeMXDPhDo if_end_short ")       
    JaTnhZWaeX()
    KsQdModhzX( IrwZJaFJTI, " IrwZJaFJTI loop_up_short ")      
    JaTnhZWaeX()
    KsQdModhzX( IvPSqNTZpN, " IvPSqNTZpN horiz_bar_short")     
    JaTnhZWaeX()
    KsQdModhzX( JAYCJiFfsS, " JAYCJiFfsS loop_out_short ")     
    JaTnhZWaeX()
    KsQdModhzX( JBQ_HVUilm, " JBQ_HVUilm cross_short ")        
    JaTnhZWaeX()
    KsQdModhzX( JBjEMlhlYZ, " JBjEMlhlYZ blank_long ")         
    return
def LVWFQFbexs( zw, text):
    global AtdaZWdHDu, AuvYTQfLWr
    AuvYTQfLWr += 6    
    AtdaZWdHDu += 78   
    for word in zw:
        for gg in word:
            if isinstance( gg, str):
                JsKHAsKxja( gg)
            else:
                KAI_KbejHa( gg)
            continue
        continue
    AuvYTQfLWr -= 6
    AtdaZWdHDu -= 78
    KJuatGQHkm( text)
    return
def rh_Show_Svg(  zfinal, zline_Nums):
    global DTzoNeECkt, DAJPZZkehP, AtdaZWdHDu, AuvYTQfLWr
    global CDxnLgBxVw, CiPNTTbEJE, CbPsPijBpc
    JmPWykfOzG( )
    AtdaZWdHDu = 1
    AuvYTQfLWr = AlKeXMetaT
    for Lnum in zline_Nums:
        rgb_color = BKllWLKmUE
        if 'O' in Lnum:
            Lnum = 'i' + Lnum   # prepend the 'i'
            rgb_color = "rgb(190,145,0)"    
        Lnum = Lnum[ : -1]  
        Lnum = "%4s" % Lnum     
        JYXwWdqplD( Lnum[0], rgb_color)
        JYXwWdqplD( Lnum[1], rgb_color)
        JYXwWdqplD( Lnum[2], rgb_color)
        JYXwWdqplD( Lnum[3], rgb_color)
        AtdaZWdHDu = 1
        AuvYTQfLWr += ARAhaWarMU
        continue
    AtdaZWdHDu = AehQIZrBOE + 4*AbCgUqXDkN
    AuvYTQfLWr = AlKeXMetaT
    for line in zfinal:
        text = line.pop()
        zsegs = line    
        zw = []
        for wordii in zsegs:
            zw.append( JToEfnhxar[ wordii])
        LVWFQFbexs( zw, text)
        continue
    DTzoNeECkt.save()
    Width_frac  = .8
    Height_frac = .83
    CiPNTTbEJE  = round( CiPNTTbEJE  * Width_frac)
    CbPsPijBpc = round( CbPsPijBpc * Height_frac)
    s =  " -------------------------------------------------\n"
    s += " You can use the following HTML code to insert the\n"
    s += " SVG image that was just made into an .html file:\n"
    s += ' <embed src="file_path.svg" width="%spx" height="%spx" />' % (CiPNTTbEJE, CbPsPijBpc)
    print( s)
    return
