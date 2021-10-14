import xml.etree.cElementTree as ET
from datetime import datetime


# Função completa o partnumber com o valor zero(0) à esquerda, e com a letra 'E' a direita do valor
def ValidateSize(value, size):
    line = ''
    newvalue = value + 'E'
    if len(newvalue) < size:
        newpartnumber = line + newvalue
        while len(newpartnumber) != size:
            line += '0'
            newpartnumber = line + newvalue
        return newpartnumber
    else:
        return newvalue


# Declaração das variáveis de ambiente
qtde_arquivo = int(input('Informe quantos arquivos deseja gerar: '))
count = 0
linesize = 12
seqnum_int = 8080

# Declaração das intruções para a criação do XML
while count < qtde_arquivo:

    print(f'Insira os dados do {count + 1}º arquivo.')

    date = datetime.now()
    date_string = date.strftime('%Y-%m-%dT%H:%M:%S')
    seqnum_str = '1' + str(seqnum_int)

    # Declaração do documento ROOT do XML
    root = ET.Element("MES_VEHICLE_STATUS_DESCRIPTOR", CISNUM="9023661", MSG_ID="1098949", OPDATE=date_string,
                      OPTYPE="NEW", SENDER="D1        ", SENDER_PLCODE="28191", SENDER_PLDESC="                    ",
                      SENDER_PLNAME="C191                ", TARGET="Vehicle_551_D1_MES_to_EXTSUPP_PIRELLI_D_SP_0031410",
                      TARGET_PLCODE="00000", TARGET_PLDESC="                    ", TARGET_PLNAME="                    ",
                      XSDVER="4.3.1")
    CISSECTION = ET.SubElement(root, "CISSECTION", CAUSAL="00000", CHANUM="KL00256", CISCKD="3", CURLIN="1", CURSTA="D",
                               CURWPL="",
                               FAM_LC="015492", FAM_MV="0515", MODCOD="675", ORGNUM="2000254", PRTSEQ="0001",
                               SEQBIW="1",
                               SEQNUM=seqnum_str,
                               SSCCOD="502", SSCDES="JEEP TA             ", STANUM="111167786",
                               VINCHA="98867516RNKL00256").text = "9023661"
    ORDERSECTION = ET.SubElement(root, "ORDERSECTION", ASSDAT="21-30", CUSCOD="2018709",
                                 DEALER="                                    ",
                                 DIFDAT="2021-08-04", ENDCUS="0", ENGCOD="130", ENGDES="MOTOR 1.3 FX AT", OPT5EA="0",
                                 ORDNUM="521626542",
                                 PSPBS="99999", SADCOD="0000", WEIGHT="0000", ZONCOD="   ")
    SINCOMSECTION = ET.SubElement(ORDERSECTION, "SINCOMSECTION", BRNCOD="57", DRVCOD="01", EXTCOD="107", INTCOD="485",
                                  MODCOD="675", MRKCOD="3491", MRPCOD="552", OPCCOD="9OZRZ", SERCOD="1", SPDCOD="0000",
                                  SPPCOD="0000", TYRCOD="00",
                                  VERCOD="16R").text = "5767516R1015529OZRZ34910000001074850000"
    CHARACTERISTICSSECTION = ET.SubElement(root, "CHARACTERISTICSSECTION")
    CHARACTERISTIC = ET.SubElement(CHARACTERISTICSSECTION, "CHARACTERISTIC", CHTYPE="001",
                                   DES_L1="FUEL                                                        ",
                                   DES_L2="FLEX                                                        ",
                                   SH_DES="FLEX      ",
                                   STRCLI="1", VAL_L1="CMB       ", VAL_L2="GA        ").text = "000056"
    PROXI_3_SECTION = ET.SubElement(root, "PROXI_3_SECTION", CONFIG="3238363735303239383230", CRCDEC="29820",
                                    HEADER="4f0c4005180018000200000000000000323335", HEADER_LENGTH="19",
                                    PRDATE="20210422",
                                    TESTER="4F55545055542D534954").text = \
        "4F0C408518001C0002000000000001004F0C400518001800020000000000000057E86F878CA00842D1330847C5103802" \
        "F118D05280751314004F023081438C20000307009A820E6300000814D4010956EB0F07A540640801221801D0143902C700F12816C00049000" \
        "A9AEF0B894900010080F22000001911211A0450000000000000000001010200000120004000000058030100080000004002000000000003000" \
        "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000" \
        "00000000000                                          "
    PARTNUMBERSSECTION = ET.SubElement(
        root, "PARTNUMBERSSECTION", SUPCOD="       ", VRTCOD="SP_0031410")

    # Declaração das variáveis para a inclusão do partnumber
    qtde_partnumber = int(
        input('Informe o total de partnumber a ser inserido: '))
    count_partnumber = 0

    # Condição verificar se o partnumber está dentro do valor necessário
    while count_partnumber < qtde_partnumber:
        partnumber = str(
            input(f'Informe o {count_partnumber + 1}º partnumber: '))

        partnumberformat = ValidateSize(partnumber, linesize)

        PARTNUMBER = ET.SubElement(PARTNUMBERSSECTION, "PARTNUMBER", PNAREA="I1", PNCARR="          ",
                                   PNDESC="CONJUNTO RODA E PNEU R19                ", PNGRUP="00000000000G",
                                   PNMATR="706101",
                                   PNPOSI="0000", PNPROX="0", PNQNTY="4", PNSUBC="0000", PNSUPP="0031410",
                                   PNUBIC="          ",
                                   RACKBIN="0000").text = partnumberformat
        count_partnumber += 1

    seqnum_int += 1

    tree = ET.ElementTree(root)
    count_string = str(count + 1)
    tree.write("filename_" + count_string + ".xml")

    count += 1
