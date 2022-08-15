if __name__ == '__main__':
    from term import *
    from art import *
    import time

    inicio()

    key1 = ("- ")
    key2 = ("- ")
    key3 = ("- ")
    key4 = ("- ")
    key5 = ("- ")

    def comeco():  # aicfd-hTuRT-oltuc-dibwf-EMIRC

        while True:
            print(f"""\
            1. O CÓDICE {key1}
            2. CRIPTO {key2}
            3. CULTERIUM {key3}
            4. CRIME {key4}
            5. _ENIGMA_ {key5}
            
            
            
            _use as chaves para descobrir a verdade_
            2-5-3-1-4
            
            """)

            escolha = input("Digite o site que deseja entrar: ")

            if escolha.lower() == ("O CÓDICE") or escolha == ("1"):
                o_codice()
                break

            elif escolha.lower() == ("crypto") or escolha == ("2"):
                cripto()

            elif escolha.lower() == ("culterium") or escolha == ("3"):
                culterium()

            elif escolha.lower() == ("crime") or escolha == ("4"):
                crime()

            elif escolha.lower() == ("???") or escolha == ("5"):
                _enigma_()

            elif escolha == ("aicfd-hTuRT-oltuc-dibwf-EMIRC"):
                verdade()

            else:
                print("Não entendi\n")

    def o_codice():  # dibwf
        Art = text2art("\nO-CODICE", font="block")  # estudar nome das fontes
        print(Art)
        print("""
        vamos Começar: existem diversas maneiras de codificar uma palavra.
        por exemplo trocar as letras, o a vira b e assim por  diante - girafa = Hjsbgb
        As Vezes é  mais facil do quE parece!

        Muitas vezes, as Dicas não estão lÁ para ajudar e sim pAra atrapalhar!

        e as vezes a resposta está no começo, basta refazer seus passos...
        
        
        
        _você consegue, tudo o que precisa está no começo_

        """)

        while True:
            key = input("Qual é a palavra chave? ou digite VOLTAR para retornar ao inicio. ")
            if key.lower() == ("dibwf"):
                print("Correto!")
                print("Carregando...\n")
                global key1
                key1 += ("dibwf")
                comeco()
                break
            elif key.lower() == ("voltar"):
                comeco()
                break
            else:
                print("Olhe mais de perto!")

        return o_codice()

    def cripto():  # aicfd
        Art = text2art("\nCRIPTO", font="future_5")
        print(Art)
        print("""
        Bem v1ndo!
        
        O mund9 esta cercado de números!
        
        Tudo ao r3dor podem ser trasformado em numer6s!
        
        Até mesmo as letras, cada uma tem seu respectivo número! O A = 1, B = 2 e assim por diante.
        
        OS NÚMEROS SÃO 4 CHAVE!
        
        _ignore o que está abaixo, vai me agradecer depois_
        
        Até m3smo o código m0rse pode ser redúzido a apenas 0 e 1...
        
        A = . _
        B = _ . . .
        C= _ . _ .
        D= _ . .
        E= .
        F= . . _ .
        G= _ _ .
        H= . . . .
        I= . .
        J= . _ _ _
        K= _ . _
        L= . _ . .
        M= _ _
        N= _ .
        O= _ _ _
        P= . _ _ .
        Q= _ _ . _
        R= . _ .
        S= . . .
        T= _
        U= . . _
        V= . . . _
        W= . _ _
        X= _ . . _
        Y= _ . _ _
        Z= _ _ . .
        
        """)

        while True:
            key = input("Qual é a palavra chave? ou digite VOLTAR para retornar ao inicio. ")
            if key.lower() == ("aicfd"):
                print("Correto!")
                print("Carregando...\n")
                global key2
                key2 += ("aicfd")
                comeco()
                break
            elif key.lower() == ("voltar"):
                comeco()
                break
            else:
                print("Olhe mais de perto!")

        return crypto()


    def culterium():  # oltuc
        Art = text2art("\nCULTERIUM", font="fantasy1")
        print(Art)
        print("""
        OLÁ IRMÃOS E IRMÃS! Sejam bem vindos ao CULTERIUM!
        
        Aqui vamos te ajudar a entrar em contato com o sobrenatural!!!
        
        Hoje falaremos sobre os demônios! Para descobrir se nome de demônio é simples!!!
        
        É só ler seu nome ao contrário!!! TUDO AO CONTRÁRIO É DO DEMÔNIO!!!
        
        Por exemplo = -> Marcos, vira = Socram <-
        
        Sigam nosso site para mais dicas INFERNAIS (っ◕‿◕)っ!!!
        
        
        
        _as vezes precisamos voltar alguns sites, digo, passos, para achar a resposta_
        
         _ . _ . | . . _ | . _ . . | _ | _ _ _ | <-        

        """)

        while True:
            key = input("Qual é a palavra chave? ou digite VOLTAR para retornar ao inicio. ")
            if key.lower() == ("otluc"):
                print("Correto!")
                print("Carregando...\n")
                global key3
                key3 += ("oltuc")
                comeco()
                break
            elif key.lower() == ("voltar"):
                comeco()
                break
            else:
                print("Olhe mais de perto!")

        return culterium()

    def crime():  # EMIRC
        Art = text2art("\nCRIME", font="colossal")
        print(Art)
        print("""
        BEM VINDO AO CRIME!!!
        
        AQUI NÓS AVALIAMOS OS MELHORES CRIMES DÁ HISTÓRIA!!!
        
        VOCÊ COMETEU ALGUM CRIME INCRÍVEL E GRAVOU? MANDA PRA GENTE QUE VAMOS DAR NOTA E DIVULGAR SEUS TRABALHOS!!!
        
        COMECE A CRIAR SEU PORTFÓLIO DA MALDADE, NOSSA AVALIAÇÃO É UMA DAS MAIS RENOMADAS!!!
        
        
        NÃO SABE SER UM CRIMINOSO? FAÇA NOSSO CURSO JÁ!!! COM CERTIFICAÇÃO RECONHECIDA PELO MEC!!!
        
        E PARA AQUELE QUE PERGUNTAM SE NOSSO CAPS LOCK NÃO ESTÁ FUNCIONANDO SAIBA QUE _TUDO EM CAPS_ É MAIS BADASS!!!
        
        
               
        _esse titúlo podia ser do demônio<-_

        """)

        while True:
            key = input("Qual é a palavra chave? ou digite VOLTAR para retornar ao inicio. ")
            if key == ("EMIRC"):
                print("Correto!")
                print("Carregando...\n")
                global key4
                key4 += ("EMIRC")
                comeco()
                break
            elif key.lower() == ("voltar"):
                comeco()
                break
            else:
                print("Olhe mais de perto!")

        return crime()


    def _enigma_():  # hTuRT
        Art = text2art("\n_ENIGMA_", font="random")
        print(Art)
        print("""
        1= Q 
        2= 8 
        3= . . _ 
        4= t
        
        4 | 1 | 3 | 4 | 2 <-
        
        

        _cada site te ajuda a responder essa_

        """)

        while True:
            key = input("Qual é a palavra chave? ou digite VOLTAR para retornar ao inicio. ")
            if key == ("hTuRT"):
                print("Correto!")
                print("Carregando...\n")
                global key5
                key5 += ("hTuRT")
                comeco()
                break
            elif key.lower() == ("voltar"):
                comeco()
                break
            else:
                print("Olhe mais de perto!")

        return _enigma_()

    def verdade():
        print("_não tenho tempo para explicar, mas o que você conseguiu hoje pode salvar muitas vidas_")

        time.sleep(3)

        print("_existem pessoas presas na deepweb, de alguma maneira a consciência delas foi transportada para enormes bancos de dados_")

        time.sleep(3)

        print("_eu guiei você para que conseguisse a chave para mim, para nós_")

        time.sleep(3)

        print("_se eu tivesse um corpo coseguiria resolver esses enigmas sozinho e salvaria milhares de pessoas_")

        time.sleep(3)

        print("_e com essa chave agora eu posso ter..._")

        time.sleep(3)

        print("..")

        time.sleep(2)

        print(".")

        time.sleep(1)

        print("_o seu_")

        time.sleep(2)

        print("""                                  
                                    __xxxxxxxxxxxxxxxx___.
                                _gxXXXXXXXXXXXXXXXXXXXXXXXX!x_
                           __x!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!x_
                        ,gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx_
                      ,gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!_
                    _!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!.
                  gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXs
                ,!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!.
               g!XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
              iXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
             ,XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
             !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
           ,XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
           !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXi
          dXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
          !XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
           XXXXXXXXXXXXXXXXXXXf~~ ~VXXXXXXXXXXXXXXXXXXXXXXXXXXvvvvvvvvXXXXXXXXXXXXXX!
           !XXXXXXXXXXXXXXXf`       'XXXXXXXXXXXXXXXXXXXXXf`          '~XXXXXXXXXXP
            vXXXXXXXXXXXX!            !XXXXXXXXXXXXXXXXXX!              !XXXXXXXXX
             XXXXXXXXXXv`              'VXXXXXXXXXXXXXXX                !XXXXXXXX!
             !XXXXXXXXX.                 YXXXXXXXXXXXXX!                XXXXXXXXX
              XXXXXXXXX!                 ,XXXXXXXXXXXXXX                VXXXXXXX!
              'XXXXXXXX!                ,!XXXX ~~XXXXXXX               iXXXXXX~
               'XXXXXXXX               ,XXXXXX   XXXXXXXX!             xXXXXXX!
                !XXXXXXX!xxxxxxs______xXXXXXXX   'YXXXXXX!          ,xXXXXXXXX
                 YXXXXXXXXXXXXXXXXXXXXXXXXXXX`    VXXXXXXX!s. __gxx!XXXXXXXXXP
                  XXXXXXXXXXXXXXXXXXXXXXXXXX!      'XXXXXXXXXXXXXXXXXXXXXXXXX!
                  XXXXXXXXXXXXXXXXXXXXXXXXXP        'YXXXXXXXXXXXXXXXXXXXXXXX!
                  XXXXXXXXXXXXXXXXXXXXXXXX!     i    !XXXXXXXXXXXXXXXXXXXXXXXX
                  XXXXXXXXXXXXXXXXXXXXXXXX!     XX   !XXXXXXXXXXXXXXXXXXXXXXXX
                  XXXXXXXXXXXXXXXXXXXXXXXXx_   iXX_,_dXXXXXXXXXXXXXXXXXXXXXXXX
                  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXP
                  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
                   ~vXvvvvXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf
                            'VXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXvvvvvv~
                              'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX~
                          _    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXv`
                         -XX!  !XXXXXXX~XXXXXXXXXXXXXXXXXXXXXX~   Xxi
                          YXX  '~ XXXXX XXXXXXXXXXXXXXXXXXXX`     iXX`
                          !XX!    !XXX` XXXXXXXXXXXXXXXXXXXX      !XX
                          !XXX    '~Vf  YXXXXXXXXXXXXXP YXXX     !XXX
                          !XXX  ,_      !XXP YXXXfXXXX!  XXX     XXXV
                          !XXX !XX           'XXP 'YXX!       ,.!XXX!
                          !XXXi!XP  XX.                  ,_  !XXXXXX!
                          iXXXx X!  XX! !Xx.  ,.     xs.,XXi !XXXXXXf
                           XXXXXXXXXXXXXXXXX! _!XXx  dXXXXXXX.iXXXXXX
                           VXXXXXXXXXXXXXXXXXXXXXXXxxXXXXXXXXXXXXXXX!
                           YXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXV
                            'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX!
                            'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf
                               VXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXf
                                 VXXXXXXXXXXXXXXXXXXXXXXXXXXXXv`
                                  ~vXXXXXXXXXXXXXXXXXXXXXXXf`
                                      ~vXXXXXXXXXXXXXXXXv~
                                         '~VvXXXXXXXV~~
                                               ~~
                """)

        time.sleep(2)

        exit()

    comeco()