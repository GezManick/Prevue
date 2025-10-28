#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import pvi
AGgQSJwB_I = '{' + '?' + '?' + '}'    
AIGClZ_ENn = '(' + ';' + ';' + ')'    
AOplPhlOqb = '©' + '©'
ARAhaWarMU = False
AbCgUqXDkN = '_eof_'
AehQIZrBOE = 31
AlKeXMetaT = 32
AtdaZWdHDu = 33
AuvYTQfLWr = 34
BFdfDKZysm = 36
BKllWLKmUE = 40
BcVqZjnKtk = 41
CDxnLgBxVw = 43
JAYCJiFfsS = 44
CiPNTTbEJE = 45
CprHciKCVV = 46
DAJPZZkehP = 47
DTzoNeECkt = 0
DUUyNBJTeg = []
DjBjZwVqxP = False
DrovcoW_RL = 0      
DuPxNRJkbT = []
DuwutE_IRa = ''
EXuxFPpjgH = []
DzochdSXbt = -1
EAPkD_zEko = []
ENdvkWgWnw = 4
EOfV_gMZJm = ENdvkWgWnw * ' '
EXuxFPpjgH = []
EYZyOBAPXU = 0
EZfPb_zbH_ = []
EgXUkjtvWL = []
EnXzdEwztn = []
EqYlh_JLKu = ""
EzmZpXdIV_ = 0    
FOcNQHECHF = 1    
FXMECaIjlp = 2   
FgUQfBVVlA = 3       
FpTCFZmNFs = 4      
FqIVSe_blf = 5           
FxIxKjavqA = 6          
GRGxjdxRIm = 7         
GRegnPACsC = 8      
GaESbtPljA = 9       
GcjXmqptTa = 10       
GvNwMZjNAf = 11      
GzTgR_wltO = 12      
HGmqRvGTnU = 13      
HVACIvhVsg = 14        
HYSfDplebQ = 15     
Hcyo_tFgBE = 16      
IBXrCwRNSJ = 17    
ISZzWAjExy = 18     
ITsRVEVyrw = 19        
IYysKfPOqP = 20         
ImhwkXUNDm = 21  
IoeMXDPhDo = 22      
IrwZJaFJTI = IoeMXDPhDo  
IvPSqNTZpN = IoeMXDPhDo
JAYCJiFfsS = 13
JBQ_HVUilm = ['#end','continue','return','break','os.exit','sys.exit','raise']
JBjEMlhlYZ = [   'if',      'for',    'while',   'def ',  'try', 'with','except','finally', 'match', 'case', 'class']
JEHBgL_WtR =   [ '#end', 'continue', 'continue', 'return', '#end', '#end',  '#end',   '#end', '#end' , '#end', 'return']
def JFShuDxxKw( line, sub_Str):
    ( at_least_1_visi, qty) = KAI_KbejHa( line)
    if not at_least_1_visi:
        return False
    visi_str = line[ qty : ]
    if len( visi_str) < len( sub_Str):
        return False
    if line[ qty : qty+len( sub_Str)] != sub_Str:
        return False
    return True
def JToEfnhxar( quote_type, ss, pt_mid):
    cond1 = False
    cond2 = False
    len_ss = len(ss)
    pt_lo = pt_mid
    while True:
        pt_lo -= 1
        if pt_lo < 0:
            return False
        if ss[pt_lo] == quote_type:
            cond1 = True
            break
    pt_hi = pt_mid
    while True:
        pt_hi += 1
        if pt_hi >= len_ss:
            return False
        if ss[pt_hi] == quote_type:
            cond2 = True
            break
    if cond1 and cond2:
        return True
    return False
def JTzwahteUo():
    global DrovcoW_RL
    DrovcoW_RL += 1
    return DrovcoW_RL
def JYXwWdqplD( ss):
    ssCopy = str( ss)
    possible_slog_tag = ssCopy[ -4 : ]
    if possible_slog_tag == AIGClZ_ENn:
        ssCopy = ssCopy[ : -4]
    if ssCopy[ -1] == 'O':
        return True
    return False
def JaTnhZWaeX():
    global EYZyOBAPXU, EZfPb_zbH_, DjBjZwVqxP
    ss = KurWDlBnwf()  
    if ss == "_eof_":
        return ( FqIVSe_blf, ss)
    if LaYsVMCXiz( ss):
        return ( IrwZJaFJTI, ss)
    if LVWFQFbexs( ss):
        return( JAYCJiFfsS, ss)
    if JFShuDxxKw( ss, "#else"):
        print( " ss:", ss)
        print( " Pyflow Error:  An `#else` appears on line %s" % str( EYZyOBAPXU))
        print( "                Perhaps #end was intended.  Please fix or alter.")
        sys.exit(1)
    if JFShuDxxKw( ss, '#end'):
        if EZfPb_zbH_[-1] != EzmZpXdIV_  and  EZfPb_zbH_[-1] != FXMECaIjlp:
            print( " Pyflow Error:  An `#end` appears to be improperly located")
            print( "                on line %s." % JmPWykfOzG( ss))
            sys.exit(1)
        if JYXwWdqplD( ss):
            ss = "©©O#end©©B" + ss[4:]
        else:
            ss = "©©R#end©©B" + ss[4:]
        return ( GvNwMZjNAf, ss)
    if JFShuDxxKw( ss, '#'):
        return (IvPSqNTZpN, ss)
    hash_on_line = False
    pt_mid = len(ss)
    while True:
        pt_mid -= 1
        if pt_mid < 0:
            break
        if ss[pt_mid] == '#':
            hash_on_line = True
            break
        continue
    if hash_on_line:
        quote_type = '"'
        D1 = JToEfnhxar( quote_type, ss, pt_mid)
        quote_type = "'"
        D2 = JToEfnhxar( quote_type, ss, pt_mid)
        if (not D1) and (not D2):
            black_part = ss[0:pt_mid]
            green_part = ss[pt_mid:]
            ss = black_part + "©©G" + green_part
            #end
        #end
    if KAoaFayWyE( ss, "if"):
        ss = "©©Rif©©B" + ss[2:]
        return ( FgUQfBVVlA, ss)
    if KAoaFayWyE( ss, "while"):
        ss = "©©Rwhile©©B" + ss[5:]
        return ( FpTCFZmNFs, ss)
    if KAoaFayWyE( ss, "for"):
        ss = "©©Rfor©©B" + ss[3:]
        return ( FpTCFZmNFs, ss)
    if KAoaFayWyE( ss, 'def '):
        ss = "©©Rdef©©B" + ss[3:]
        return ( ImhwkXUNDm, ss)
    if KAoaFayWyE( ss, "else"):
        if not ( EZfPb_zbH_[-1] == EzmZpXdIV_  or  EZfPb_zbH_[-1] == FXMECaIjlp):
            print( "\n Pyflow Error:  The `else` on line %s appears to be" %  JmPWykfOzG( ss))
            print( "  misplaced.  Perhaps you used one of these keywords:")
            print( "  ( return, break, continue) between an `if` and its")
            print( "  corresponding `else`.  If so, then you broke Pyflow")
            print( "  rule 2.  If that's the case, try rewriting your")
            print( "  `if` block without using `else`.")
            sys.exit(1)
        if EZfPb_zbH_[-1] == FXMECaIjlp:    
            s ="\n Pyflow Error:  In Python, an `if` statement can have\n"
            s += " only one `else`.  The `else` on line %s\n" % JmPWykfOzG( ss)
            s += " appears to be the second `else` for the previous `if`.\n"
            print( s)
            sys.exit(1)
        if EZfPb_zbH_[-1] == EzmZpXdIV_:
            EZfPb_zbH_[-1] = FXMECaIjlp
        ss = "©©Relse©©B" + ss[4:]
        return ( FxIxKjavqA, ss)
    if KAoaFayWyE( ss, "try"):
        ss = "©©Rtry©©B" + ss[3:]
        return ( FgUQfBVVlA, ss)
    if KAoaFayWyE( ss, "with"):
        ss = "©©Rwith©©B" + ss[4:]
        return ( FgUQfBVVlA, ss)
    if KAoaFayWyE( ss, "except"):
        ss = "©©Rexcept©©B" + ss[6:]
        return ( FgUQfBVVlA, ss)
    if KAoaFayWyE( ss, "elif"):
        print( " Pyflow Error: The `elif` on line %s is not" % JmPWykfOzG( ss))
        print( "               supported by the current version of Pyflow.")
        sys.exit(1)
    if KAoaFayWyE( ss, "break"):
        if (FOcNQHECHF not in EZfPb_zbH_) and (ISZzWAjExy not in EZfPb_zbH_):
            print( " Pyflow Error:  A problem is seen on line %s." % JmPWykfOzG( ss))
            print( " There is a `break` statement, but seemingly no prior loop")
            print( " to break from.  See the above mirror dump.")
            sys.exit(1)
        ss = "©©Rbreak©©B" + ss[5:]
        return ( GzTgR_wltO, ss)
    if KAoaFayWyE( ss, "#end"):
        if JYXwWdqplD( ss):
            ss = "©©O#end©©B" + ss[4:]    
        else:
            ss = "©©R#end©©B" + ss[4:]
        return ( GRGxjdxRIm, ss)
    if KAoaFayWyE( ss, "return"):
        if HVACIvhVsg not in EZfPb_zbH_:  
            print( " Pyflow Warning:")
            print( " There is a `return` statement on line %s," % JmPWykfOzG( ss))
            print( " but no function definition is on the stack.")
        if JYXwWdqplD( ss):
            ss = "©©Oreturn©©B" + ss[6:]  
        else:
            ss = "©©Rreturn©©B" + ss[6:]
        return ( GRegnPACsC, ss)
    if KAoaFayWyE( ss, "continue"):
        if FOcNQHECHF not in EZfPb_zbH_:
            s = " Pyflow Warning:  There is a `continue` statement on\n"
            s += "                 line %s, but no prior loop." % JmPWykfOzG( ss)
            print( s)
        if JYXwWdqplD( ss):
            ss = "©©Ocontinue©©B" + ss[8:]    
        else:
            ss = "©©Rcontinue©©B" + ss[8:]
        return ( GcjXmqptTa, ss)
    if KAoaFayWyE( ss, "raise "):
        ss = "©©Rraise©©B" + ss[5:]
        return ( GRegnPACsC, ss)
    if KAoaFayWyE( ss, "finally"):
        ss = "©©Rexcept©©B" + ss[6:]
        return ( FgUQfBVVlA, ss)
    if KAoaFayWyE( ss, "sys.exit"):
        ss = "©©Rsys.exit©©B" + ss[8:]
        return ( GRegnPACsC, ss)
    if KAoaFayWyE( ss, "os.exit"):
        ss = "©©Ros.exit©©B" + ss[7:]
        return ( GRegnPACsC, ss)
    return ( FqIVSe_blf, ss)
def JhkgQZDktM():
    global EZfPb_zbH_, EgXUkjtvWL, EqYlh_JLKu, EYZyOBAPXU
    while True:
        ( EqYlh_JLKu, text) = JaTnhZWaeX()  
        EZfPb_zbH_.append( EqYlh_JLKu)
        if text == AbCgUqXDkN:
            return
        one_line = list( EZfPb_zbH_)   
        one_line.append( text)
        NYe_UxWFaP( one_line)
        EZfPb_zbH_.pop()               
        if LaYsVMCXiz( text):
            continue
        if EqYlh_JLKu == FgUQfBVVlA:
            EZfPb_zbH_.append( EzmZpXdIV_)
            continue
        if EqYlh_JLKu == FpTCFZmNFs:
            EZfPb_zbH_.append( FOcNQHECHF)
            continue
        if EqYlh_JLKu == ImhwkXUNDm:
            EZfPb_zbH_.append( HVACIvhVsg)
            continue
        if EqYlh_JLKu == GvNwMZjNAf:
            EZfPb_zbH_.pop()
            continue
        if EqYlh_JLKu == GcjXmqptTa:
            EZfPb_zbH_.pop()
            continue
        if EqYlh_JLKu == GzTgR_wltO:
            EZfPb_zbH_.pop()
            continue
        if EqYlh_JLKu == GRegnPACsC:
            EZfPb_zbH_.pop()
            continue
        continue
def JmPWykfOzG( line):
    ll2 = str( line)
    iitag = ll2.find( AGgQSJwB_I)
    iiNum_Str = iitag + 4
    Num_str = line[ iiNum_Str : -1]
    return Num_str
def JsKHAsKxja():
    global EgXUkjtvWL, EnXzdEwztn, EYZyOBAPXU, EYZyOBAPXU
    EYZyOBAPXU = 0
    EnXzdEwztn = []
    for zST_line in EgXUkjtvWL:   
        beyond_ii = len( zST_line)
        text_ii = beyond_ii - 1
        final_segii = text_ii - 1
        text = zST_line.pop()
        if LaYsVMCXiz( text):
            text = (2*EOfV_gMZJm) + text
            seg_count = len( zST_line)
            indents_to_chop = seg_count
            qty_spaces_to_chop = indents_to_chop * ENdvkWgWnw
            ( saw_visi, qty_spaces) = KAI_KbejHa( text)
            if saw_visi and (qty_spaces >= qty_spaces_to_chop):
                text = text[ qty_spaces_to_chop : ]     
                #end
            text = ' ' + text
            #end
        zST_line.append( text)
        if zST_line[ final_segii] == FxIxKjavqA:
            if (final_segii - 1) == -1:   
                print( " Pyflow Error: The `else` on line %s" % str( EYZyOBAPXU))
                print( " appears to be misplaced.")
                sys.exit(1)
            lefty_seg = zST_line[ final_segii - 1]
            if not( lefty_seg == EzmZpXdIV_  or  lefty_seg == FXMECaIjlp):
                s =  " Pyflow Error: The `else` on line %s\n" % str( EYZyOBAPXU)
                s += " needs to be indented once with respect\n"
                s += " to an above `if`.\n"
                print( s)
                sys.exit(1)
            zST_line[ final_segii - 1] = FXMECaIjlp
            the_text = zST_line.pop()              
            the_final_seg = zST_line.pop()         
            zST_line.pop()                         
            zST_line.append( the_final_seg)        
            the_text = EOfV_gMZJm + '  ' + the_text
            zST_line.append( the_text)             
            NencQayfQa( zST_line)
            line = zST_line[ -1]                 
            line = line[ ENdvkWgWnw : ]   
            zST_line[ -1] = line                 
            continue 
        if zST_line[ final_segii] == GvNwMZjNAf:
            zST_line[ final_segii] = HVACIvhVsg
            if (final_segii - 1) == -1:
                print( " Pyflow Error:  An #end on line %s appears to be misplaced." % str( EYZyOBAPXU))
                sys.exit(1)
            seg_type = zST_line[ final_segii - 1]
            if not ( seg_type == EzmZpXdIV_  or  seg_type == FXMECaIjlp):
                print( " Pyflow Error:  An #end needs to be under an `if`.")
                print( "                The #end was seen on line %s" % str( EYZyOBAPXU))
                sys.exit(1)
            zST_line[ final_segii - 1] = GvNwMZjNAf   
            NencQayfQa( zST_line)         
            continue 
        if zST_line[ final_segii] == GcjXmqptTa:
            zST_line[ final_segii] = GRGxjdxRIm
            ii_seg = final_segii
            while True:
                ii_seg -= 1  
                if ii_seg == -1:
                    print( "\n Pyflow Error: The `continue` on line %s:" % str( EYZyOBAPXU))
                    print(  "                appears to be misplaced.")
                    break
                if zST_line[ ii_seg] == EzmZpXdIV_  or  zST_line[ ii_seg] == FXMECaIjlp:
                    zST_line[ ii_seg] = ITsRVEVyrw       
                    continue   
                if zST_line[ ii_seg] == FOcNQHECHF:
                    zST_line[ ii_seg] = Hcyo_tFgBE   
                    break
                break
            NencQayfQa( zST_line)
            continue 
        if zST_line[ final_segii] == GzTgR_wltO:
            zST_line[ final_segii] = GRGxjdxRIm
            ii_seg = final_segii
            while True:
                ii_seg -= 1  
                if ii_seg == -1:
                    print( "\n Pyflow Error: The `break` the line being examined")
                    print(  "                appears to be misplaced.")
                    sys.exit(1)
                seggy = zST_line[ ii_seg]
                if seggy == EzmZpXdIV_ or seggy == FXMECaIjlp:
                    zST_line[ ii_seg] = ITsRVEVyrw       
                    continue
                if zST_line[ ii_seg] == FOcNQHECHF:
                    zST_line[ ii_seg] = ISZzWAjExy    
                    break
                continue
            NencQayfQa( zST_line)
            continue 
        NencQayfQa( zST_line)
        continue  
    return
def KAI_KbejHa( line):
    saw_visi = False
    qty_spaces = 0
    for ch in line:
        if ch == ' ':
            qty_spaces += 1
        else:
            saw_visi = True
            break
        continue
    return ( saw_visi, qty_spaces)
def KAoaFayWyE( line, sub_str):
    lss = len( sub_str)
    if line[ : lss] == sub_str:
        return True
    return False
def KJuatGQHkm( line):
    count = 0
    for ch in line:
        if ch != ' ':
            break
        count += 1
        continue
    line = line[ count : ]
    return line
def KsQdModhzX( line):
    is_true_comment = False
    while True:
        if JFShuDxxKw( line, '#end'):
            break
        if JFShuDxxKw( line, '#else'):    # a user mistake
            break
        is_true_comment = JFShuDxxKw( line, '#')
        break
    return is_true_comment
def KurWDlBnwf():
    global p4_line_ii  
    p4_line_ii += 1
    if p4_line_ii >= len( EXuxFPpjgH):
        return( "_eof_")
    line = EXuxFPpjgH[ p4_line_ii]          
    is_slog = LaYsVMCXiz( line)
    if not is_slog:
        is_true_comment = KsQdModhzX( line)
    if not (is_slog or is_true_comment):
        line = KJuatGQHkm( line)
    return line
def LHrSNWXTCi( line):
    global JBQ_HVUilm, JBjEMlhlYZ, JEHBgL_WtR
    if line == '_eof_':
        return ( 'CDxnLgBxVw', AbCgUqXDkN)
    ii = 0
    len_JBjEMlhlYZ = len(JBjEMlhlYZ)
    for ii in range( 0, len_JBjEMlhlYZ):
        word = JBjEMlhlYZ[ ii]
        if JFShuDxxKw( line, word):
            tail_word = JEHBgL_WtR[ ii]
            return ( 'CiPNTTbEJE', tail_word)
        continue
    len_JBQ_HVUilm = len(JBQ_HVUilm)
    for ii in range( 0, len_JBQ_HVUilm):
        word = JBQ_HVUilm[ ii]
        if JFShuDxxKw( line, word):
            return ( 'DAJPZZkehP', 'XDED...')
        continue
    if JFShuDxxKw( line, 'else:'):
        return ( 'CDxnLgBxVw', 'XELS...')
    return ( 'CDxnLgBxVw', 'XSTM...')
def LIzqkPZaMD( line):
    EnXzdEwztn.append( line)
    print( line)
    return
def LVWFQFbexs( line):
    ( saw_visi, qty_spaces) = KAI_KbejHa( line)
    ii = line.find( AGgQSJwB_I)
    is_blank = (ii == qty_spaces)
    return is_blank
def LaYsVMCXiz( line):
    if line[ -4:] == AIGClZ_ENn:
        return True
    return False
def LdsiCcWpei():
    global DzochdSXbt, EYZyOBAPXU
    while True:
        EYZyOBAPXU += 1
        DzochdSXbt += 1
        if DzochdSXbt >= len( EXuxFPpjgH):
            return ( 'c', '_eof_')
        line = EXuxFPpjgH[ DzochdSXbt]
        if LaYsVMCXiz( line):
            return ( 's', line)  
        ( saw_visi, qty_spaces) = KAI_KbejHa( line)
        if not saw_visi:
            return ( 'f', '')    
        if LVWFQFbexs( line):
            return ( 'f', line)  
        if JFShuDxxKw( line, '#end'):
            return ( 'c', line)  
        if JFShuDxxKw( line, '#'):  # if a regular comment
            return ( 'f', line)  
        break
    return ( 'c', line)   
def LfHhgJitPW( line, triple_quote):
    ch_type = triple_quote[0]
    lin2 = str(  line)  
    ii_found = lin2.find( triple_quote)
    if ii_found == -1:  
        return False
    lin2 = lin2[ ii_found+3 : ]
    ii_found = lin2.find( triple_quote)
    if ii_found == -1:  
        return False
    return True
def LgprYbnzbz( line):
    global DjBjZwVqxP
    if LfHhgJitPW( line, "'''") or LfHhgJitPW( line, '"""'):
        return True
    cond1 = JFShuDxxKw( line, '"""')
    cond2 = JFShuDxxKw( line, "'''")
    marked_line = cond1 or cond2
    if marked_line:
        DjBjZwVqxP = not DjBjZwVqxP     
        #end
    slog_region = marked_line or DjBjZwVqxP
    return slog_region
def LlOjiiWbNW( line):
    if LgprYbnzbz( line):
        longer_line = line + AIGClZ_ENn
        return longer_line
    return line
def LtIVYTEkEH( line):
    EnXzdEwztn.append( ('i', line))
    return
def LuAnXGxwfl( line):
    EnXzdEwztn.append( ('f', line))
    return
def MAyzAoGxhz( line):
    EnXzdEwztn.append( ('c', line))
    return
def MEaJctuuvi( msg_str):
    global EXuxFPpjgH, EnXzdEwztn
    for line in EnXzdEwztn:
        pass
    return
def MLGimmcpMp():
    ( code_type, line) = LdsiCcWpei()
    ( indent_type, tail) = LHrSNWXTCi( line)
    return ( indent_type, tail, code_type, line)
def MMXL_tzcun():
    global EXuxFPpjgH, EAPkD_zEko, EYZyOBAPXU, EnXzdEwztn, EOfV_gMZJm
    global ENdvkWgWnw, DzochdSXbt, DTzoNeECkt
    global slog_region, directive, EYZyOBAPXU
    for line in EXuxFPpjgH:     
        EYZyOBAPXU += 1
        line.expandtabs( tabsize = ENdvkWgWnw)   
        len_line = len( line)
        if len_line > DTzoNeECkt:
            DTzoNeECkt = len_line
        ( at_least_1_visi, count) = KAI_KbejHa( line)
        tail = AGgQSJwB_I
        tail += str( EYZyOBAPXU)
        tail +='B'
        line += tail
        line = LlOjiiWbNW( line)
        if JFShuDxxKw( line, 'else'):
            line = EOfV_gMZJm + line
            #end
        NDOxgTbRzr( line)
        continue
    return
def MOmxX_TCAW():
    global EnXzdEwztn, EXuxFPpjgH
    EXuxFPpjgH = list( EnXzdEwztn)
    EnXzdEwztn = []
    return
def NDOxgTbRzr( line):
    EnXzdEwztn.append( line)
    return
def NKeSUcuxYF( pass_str, line):
    iiLnT = line.find( AGgQSJwB_I)
    if iiLnT != -1:   
        iiNum = iiLnT + 4
        iiST = line.find( AIGClZ_ENn)
        if iiST != -1:    
            num_str_raw = line[ iiNum: iiST]
        else:
            num_str_raw = line[ iiNum: ]
            #end
        color_code_letter = num_str_raw[-1]
        EYZyOBAPXU = num_str_raw[ :-1]      
        s = ''
        if color_code_letter == 'O':     
            s = 'i'
        EYZyOBAPXU = s + EYZyOBAPXU
        print( " %s: %s" % (pass_str, EYZyOBAPXU))
        #end
    return
def NVo_JOHlLx( line):
    global ARAhaWarMU, EnXzdEwztn
    if ARAhaWarMU:
        NKeSUcuxYF( "P2", line)
    else:
        pass
    EnXzdEwztn.append( line)
    return
def NYe_UxWFaP( line):
    global ARAhaWarMU, EgXUkjtvWL
    text = line[-1]
    if ARAhaWarMU:
        NKeSUcuxYF( "P4", text)
    else:
        pass
    EgXUkjtvWL.append( line)
    return
def NencQayfQa( line):
    global ARAhaWarMU, EnXzdEwztn
    text = line[-1]
    if ARAhaWarMU:
        NKeSUcuxYF( "P5", text)
    else:
        pass
    EnXzdEwztn.append( line)
    return
def NfxxdUqMRI():
    global EnXzdEwztn, EXuxFPpjgH, EYZyOBAPXU, DjBjZwVqxP
    EYZyOBAPXU = 0  
    DUUyNBJTeg = []
    dif_buf = []
    DjBjZwVqxP = False
    got_AbCgUqXDkN = False
    while True:
        (prev_indent_type, prev_tail, prev_code_type, prev_line) = MLGimmcpMp()
        prev_tup = ( prev_indent_type, prev_tail, prev_code_type, prev_line)
        prev_EYZyOBAPXU = EYZyOBAPXU
        if prev_code_type != 'c':
            NVo_JOHlLx( prev_line)
            continue
        break
    while True:
        if prev_indent_type == "CiPNTTbEJE":
            DUUyNBJTeg.append( prev_tail)
        while True:
            ( cur_indent_type, cur_tail, cur_code_type, cur_line) = MLGimmcpMp()
            if cur_line == '_eof_':
                got_AbCgUqXDkN = True
            cur_tup = ( cur_indent_type, cur_tail, cur_code_type, cur_line)
            cur_EYZyOBAPXU = EYZyOBAPXU
            if cur_code_type == 'c':
                break
            dif_buf.append( (cur_code_type, cur_line) )
            continue
        ( prev_at_least_1_visi, prev_qty_spaces) = KAI_KbejHa( prev_line)
        prev_indent_lev = prev_qty_spaces // ENdvkWgWnw
        ( cur_at_least_1_visi, cur_qty_spaces) = KAI_KbejHa( cur_line)
        cur_indent_lev = cur_qty_spaces // ENdvkWgWnw
        qty_pops_needed = prev_indent_lev - cur_indent_lev
        NVo_JOHlLx( prev_line)
        if qty_pops_needed < 1:  
            while len( dif_buf) > 0:
                ( code_type,  line) = dif_buf.pop(0)
                NVo_JOHlLx( line)
                continue
        else:
            temp_buf = []
            while len( dif_buf) > 0:
                ( code_type,  line) = dif_buf.pop(0)
                if code_type == 's':    
                    NVo_JOHlLx( line)
                else:
                    temp_buf.append( ( code_type,  line))
                continue
            dif_buf = temp_buf
            #end
        while qty_pops_needed >= 1:
            if prev_indent_type == 'DAJPZZkehP':
                DUUyNBJTeg.pop()                  
            else:
                default_tail = DUUyNBJTeg.pop()               
                string = prev_indent_lev * EOfV_gMZJm
                iLine = string + default_tail
                numb = JTzwahteUo()
                iLine += AGgQSJwB_I + str( numb) + 'O'   
                NVo_JOHlLx( iLine)
                #end
            qty_pops_needed -= 1
            prev_indent_lev -= 1
            prev_indent_type = 'not dedent'
            continue
        while len( dif_buf) > 0:
            ( code_type,  line) = dif_buf.pop(0)
            NVo_JOHlLx( line)
            continue
        if got_AbCgUqXDkN:
            NVo_JOHlLx( cur_line)
            return
        ( prev_indent_type, prev_tail, prev_code_type, prev_line) = cur_tup
        prev_tup = ( prev_indent_type, prev_tail, prev_code_type, prev_line)
        prev_EYZyOBAPXU = cur_EYZyOBAPXU        
        continue
    print( " got to end of NfxxdUqMRI")
    return
def NuTGHMiSbh():    
    global DuwutE_IRa, R_input_file_path, R_Svg_File_Path, ARAhaWarMU
    len_argv = len( sys.argv)
    if len_argv < 2 or len_argv > 3:
        print( " Usage:  no_trace  or  with_trace:")
        print( "     pyf <name>[.py]")
        print( " or")
        print( "     pyf -t <name>[.py]")
        sys.exit(1)
    trace_flag = sys.argv[ 1]
    if sys.argv[ 1] == '-t':
        ARAhaWarMU = True
        DuwutE_IRa = sys.argv[ 2]
    else:
        DuwutE_IRa = sys.argv[ 1]    
    R_input_file_path = str( DuwutE_IRa)
    R_Svg_File_Path   = str( DuwutE_IRa) + ".svg"
    return ( R_Svg_File_Path, R_input_file_path)
def OEYzpmEuEx():   
    global DuPxNRJkbT, DuwutE_IRa
    if not os.path.isfile( DuwutE_IRa):
        print( "\n Pyflow Error:  The file %s does not exist." % DuwutE_IRa)
        sys.exit(1)
    readable = os.access( DuwutE_IRa, os.R_OK)
    if not readable:
        print( "\n Pyflow Error:  The file %s is not readable." % DuwutE_IRa)
        sys.exit(1)
    with open( DuwutE_IRa, 'r', encoding='utf-8') as f_obj:  
        big_string = f_obj.read()
        #end
    return big_string
def OGoapksfmu( BStr):
    line = ''
    ch = ''
    ii = -1
    while True:  
        ii += 1
        if ii >= len( BStr):
            break
        ch = BStr[ ii]
        if ch != '\n':
            line += ch
        else:
            EnXzdEwztn.append( line)
            line = ''
        continue
    EnXzdEwztn.append( line)
    return EnXzdEwztn
def main():
    global EnXzdEwztn, EXuxFPpjgH, EYZyOBAPXU, DzochdSXbt, DjBjZwVqxP, EZfPb_zbH_
    global ARAhaWarMU, p4_line_ii, p4_DjBjZwVqxP, DTzoNeECkt
    ( R_Svg_File_Path, R_input_file_path) = NuTGHMiSbh()
    big_string = OEYzpmEuEx()  
    EnXzdEwztn = []   
    EnXzdEwztn = OGoapksfmu( big_string)
    EXuxFPpjgH = list( EnXzdEwztn)    
    EnXzdEwztn = []               
    EYZyOBAPXU = 0
    DzochdSXbt = -1
    DjBjZwVqxP = False
    EZfPb_zbH_ = []
    MMXL_tzcun()     
    if ARAhaWarMU:
        print( "----------------------")
    MEaJctuuvi( " P1 output:")
    MOmxX_TCAW()
    EYZyOBAPXU = 0
    DzochdSXbt = -1
    DjBjZwVqxP = False
    EZfPb_zbH_ = []
    NfxxdUqMRI()     
    if ARAhaWarMU:
        print( "----------------------")
    MEaJctuuvi( " P2 output:")
    MOmxX_TCAW()
    EYZyOBAPXU = 0
    DzochdSXbt = -1
    DjBjZwVqxP = False
    EZfPb_zbH_ = []
    p4_line_ii = -1
    p4_DjBjZwVqxP = False
    JhkgQZDktM()     
    if ARAhaWarMU:
        print( "----------------------")
    EYZyOBAPXU = 0
    DzochdSXbt = -1
    DjBjZwVqxP = False
    EZfPb_zbH_ = []
    JsKHAsKxja()     
    MEaJctuuvi( " P5 output:")
    zline_Nums = []  
    zfinal = []   
    for line_w_segs in EnXzdEwztn:
        text = str( line_w_segs[ -1])
        ii_slogTag = text.find( AIGClZ_ENn)
        text_is_a_slog = False
        if ii_slogTag != -1:    
            text_is_a_slog = True
            text = text[ : ii_slogTag]    
        ii_AGgQSJwB_I = text.find( AGgQSJwB_I)
        lnum_raw = text[ ii_AGgQSJwB_I : ]     
        text = text[ : ii_AGgQSJwB_I]
        lnum_color = lnum_raw[-1]
        lnum = lnum_raw[ 4: -1]         
        stringy = lnum + lnum_color
        zline_Nums.append( stringy)
        if text_is_a_slog:
            text = text + AIGClZ_ENn
        line_w_segs.pop()           
        is_true_comment = False
        if not text_is_a_slog:
            is_true_comment = KsQdModhzX( text)
            if is_true_comment:
                indents_to_chop = len( line_w_segs) - 1
                ( saw_visi, qty_spaces) = KAI_KbejHa( text)
                indents_to_chop = round( qty_spaces / ENdvkWgWnw)
                if indents_to_chop < 0:
                    indents_to_chop = 0
                spaces_to_chop = ENdvkWgWnw * indents_to_chop
                text = text[ spaces_to_chop : ]
                text = '©©G  ' + EOfV_gMZJm + text
        if text_is_a_slog:
            text = '©©D' + text       
        else:
            text = text  
        line_w_segs.append( text)       
        zfinal.append( line_w_segs)     
        continue
    line_count_to_show = len( zfinal)
    pvi.rh_Init_Dwg( line_count_to_show, DTzoNeECkt, R_input_file_path, R_Svg_File_Path)
    pvi.rh_Show_Svg( zfinal, zline_Nums)
    print("------------------------------------------------")
    qty = JTzwahteUo()
    qty -= 1
    print(" Well done!  Pyflow inserted %d lines." % qty)
    print("             Look for the .svg output as %s" % R_Svg_File_Path)
    return
if __name__ == "__main__":
    main()
