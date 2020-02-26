<?xml version="1.0" encoding="windows-1251"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="1.0">
    <xsl:output method="html"></xsl:output>
    <xsl:template match="/">
        <xsl:apply-templates/>
    </xsl:template>
    <xsl:template match="/СвЮЛ"> 
           <div>                   
                   <table class="table table-sm" border="0" cellpadding="1" align="center" width="100%">
                       <tr id= "General">                           
                           <td align="center">ВЫПИСКА</td>                             
                       </tr>
                       <tr>
                          <td align="center">из Единого государственного реестра юридических лиц</td>                                               
                       </tr>
                       <tr> </tr>
                       <tr>
                           <td align="center">
                              <xsl:value-of select="СвНаимЮЛ/@НаимЮЛПолн"/>                           
                          </td>                                            
                       </tr>
                       <tr>
                           <td align="rigth">
                            ОГРН <xsl:value-of select="@ОГРН"/>
                          </td>                                               
                       </tr>
                       <tr>
                           <td align="rigth">
                               ИНН/КПП <xsl:value-of select="@ИНН"/>/<xsl:value-of select="@КПП"/>
                           </td>                                               
                       </tr>
                       <tr>
                           <td align="rigth">
                               по состоянию на <xsl:value-of select="@ДатаВып"/>
                           </td>
                       </tr>
                    </table> 
                   <table class="table table-sm table-bordered" border="1" cellpadding="3" align="center" width="100%">
                    <tr>
                        <th width="7%">N п/п</th>
                        <th>Наименование показателя</th>
                        <th>Значение показателя</th>
                    </tr>
                       <tr>
                           <td align="center">1</td>
                           <td align="center">2</td>
                           <td align="center">3</td>
                       </tr>  
                       <xsl:apply-templates select="СвНаимЮЛ"/>                                  
                       <xsl:apply-templates select="СвАдресЮЛ"/>
                       <xsl:apply-templates select="СвАдрЭлПочты"/>
                       <xsl:apply-templates select="СвОбрЮЛ"/>
                       <xsl:apply-templates select="СвРегОрг"/>
                       <xsl:for-each select="СвСтатус">
                           <xsl:call-template name="СвСтатус"/>
                       </xsl:for-each>                       
                       <xsl:apply-templates select="СвПрекрЮЛ"/>
                       <xsl:apply-templates select="СвУчетНО"/>
                       <xsl:apply-templates select="СвРегПФ"/>
                       <xsl:apply-templates select="СвРегФСС"/> 
                       <xsl:apply-templates select="СвУстКап"/>
                       <xsl:apply-templates select="СвТипУстКап"/>
                       <xsl:if test="СвУпрОрг">
                           <tr>
                               <td id ="SvUpOrg" colspan="3" style="text-align:center"><b>Сведения об управляющей организации</b></td>
                           </tr>
                           <xsl:for-each select="СвУпрОрг">
                               <xsl:call-template name="СвУпрОрг"/>                            
                           </xsl:for-each>
                       </xsl:if>                 
                       <xsl:if test="СведДолжнФЛ">
                           <tr>
                                <td id="SvDoljFL" colspan="3" style="text-align:center"><b>Сведения о лицах, имеющих право без доверенности действовать от имени юридического лица  </b> </td>
                            </tr>
                            <xsl:for-each select="СведДолжнФЛ">
                                <xsl:call-template name="СведДолжнФЛ"/>                            
                           </xsl:for-each>
                       </xsl:if>
                       <xsl:if test="СвУчредит">
                           <tr>
                               <td id="SvUchr" colspan="3" style="text-align:center"><b>Сведения об учредителях (участниках) юридического лица </b> </td>
                           </tr>
                           <xsl:for-each select="СвУчредит">
                               <xsl:call-template name="СвУчредит"/> 
                           </xsl:for-each>
                           
                       </xsl:if>
                       <xsl:apply-templates select="СвДоляООО"/>
                       <xsl:apply-templates select="СвДержРеестрАО"/>
                       <xsl:if test="СвОКВЭД">
                            <tr>
                                <td id="SvOKWED" colspan="3" style="text-align:center"><b>Сведения о видах экономической деятельности по Общероссийскому классификатору видов экономической деятельности </b> </td>
                            </tr>                       
                            <xsl:for-each select="СвОКВЭД">
                                <xsl:call-template name="СвОКВЭД"/>                               
                            </xsl:for-each>
                       </xsl:if>
                       <xsl:if test="СвЛицензия">
                           <tr>
                           <td id="SvLicense" colspan="3" style="text-align:center"><b>Сведения о лицензиях, выданных ЮЛ </b> </td>
                           </tr>
                            <xsl:for-each select="СвЛицензия">
                                <xsl:call-template name="СвЛицензия"/>                             
                            </xsl:for-each>
                       </xsl:if>
                       <xsl:apply-templates select="СвПодразд"/>                       
                       <xsl:if test="СвРеорг">
                           <tr>
                               <td id="SvReorg" colspan="3" style="text-align:center"><b>Сведения об участии в реорганизации </b> </td>
                           </tr>
                           <xsl:for-each select="СвРеорг">
                                <xsl:call-template name="СвРеорг"/>   
                           </xsl:for-each>
                       </xsl:if>
                       <xsl:if test="СвПредш">
                           <tr>
                               <td id="SvPredSh" colspan="3" style="text-align:center"><b>Сведения о правопредшественнике </b> </td>
                           </tr>
                       <xsl:for-each select="СвПредш">
                           <xsl:call-template name="СвПредш"/>   
                       </xsl:for-each>
                       </xsl:if>
                       <xsl:if test="СвКФХПредш">
                           <tr>
                               <td id="SvKFHPredSh" colspan="3" style="text-align:center"><b>Сведения о крестьянском (фермерском) хозяйстве, на базе имущества которого создано юридическое лицо </b> </td>
                           </tr>
                       <xsl:for-each select="СвКФХПредш">
                           <xsl:call-template name="СвКФХПредш"/>   
                       </xsl:for-each>
                       </xsl:if>
                       <xsl:if test="СвПреем">
                           <tr>
                               <td id="SvPreem" colspan="3" style="text-align:center"><b>Сведения о крестьянском (фермерском) хозяйстве, на базе имущества которого создано юридическое лицо </b> </td>
                           </tr>
                        <xsl:for-each select="СвПреем">
                            <xsl:call-template name="СвПреем"/>   
                        </xsl:for-each>
                             
                       </xsl:if>
                       <xsl:apply-templates select="СвКФХПреем"/>
                       <tr>
                           <td id="EGRULrecords" colspan="3" style="text-align:center"><b>Сведения о записях, внесенных в Единый государственный реестр юридических лиц </b> </td>
                       </tr>
                       <xsl:for-each select="СвЗапЕГРЮЛ">
                           <xsl:call-template name="СвЗапЕГРЮЛ"/>   
                       </xsl:for-each>              
                   </table> 
                   <div id="bottom" class="anchor"></div>
               </div>
              
            </xsl:template>
        <xsl:template match="СвНаимЮЛ">
            
            <tr>
                <td id= "Name" colspan="3" style="text-align:center"><b>Наименование </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">Полное наименование</td>
                <td align="left"><xsl:value-of select="@НаимЮЛПолн"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">Сокращенное наименование</td>
                <td align="left"><xsl:value-of select="@НаимЮЛСокр"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td align="left"><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>
        </xsl:template>
        <xsl:template match="СвАдресЮЛ">
            <tr>
                <td id = "Address" colspan="3" style="text-align:center"><b>Адрес (место нахождения) </b> </td>
                <xsl:apply-templates select="АдресРФ">
                </xsl:apply-templates>
            </tr>          
            <xsl:for-each select="СвНедАдресЮЛ">
                <xsl:call-template name="СвНедАдресЮЛ"/>                             
            </xsl:for-each>                 
        </xsl:template>
        <xsl:template name="СвНедАдресЮЛ">
            <tr>                      
                <td class="num" align="center"></td>
                <td align="left">Дополнительные сведения </td>
                <td align="left"><xsl:value-of select="@ТекстНедАдресЮЛ"/></td>
            </tr>
            <xsl:if test="РешСудНедАдр">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения о решении суда, на основании которого адрес признан недостоверным</td>
                    <td><xsl:value-of select="РешСудНедАдр/@КНаимСуда"/> <br/>
                        Решение №<xsl:value-of select="РешСудНедАдр/@Номер"/> от <xsl:value-of select="РешСудНедАдр/@Дата"/>
                    </td>              
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="АдресРФ"> 
            <tr>
                <td class="num" align="center"></td>
                <td align="left">Почтовый индекс</td>
                <td align="left"><xsl:value-of select="@Индекс"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">Субъект Российской Федерации</td>
                <td align="left"><xsl:value-of select="@КодРегион"/> - <xsl:value-of select="Регион/@ТипРегион"/>&#160;<xsl:value-of select="Регион/@НаимРегион"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">Код адреса по КЛАДР</td>
                <td align="left"><xsl:value-of select="@КодАдрКладр"/></td>
            </tr> 
            <xsl:if test="Город">
            <tr>
                <td class="num" align="center"></td>
                <td align="left">Город (волость и т.п.)</td>
                <td align="left"><xsl:value-of select="Город/@ТипГород"/>&#160;<xsl:value-of select="Город/@НаимГород"/></td>
            </tr>
            </xsl:if>    
            <xsl:if test="НаселПункт">
                <tr>
                    <td class="num" align="center"></td>
                    <td align="left">Населенный пункт (село и т.п.)</td>
                    <td align="left"><xsl:value-of select="НаселПункт/@ТипНаселПункт"/>&#160;<xsl:value-of select="НаселПункт/@НаимНаселПункт"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="Район">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Район (улус и т.п.)</td>
                    <td><xsl:value-of select="Район/@ТипРайон"/>&#160;<xsl:value-of select="Район/@НаимРайон"/></td>
                </tr>
                
            </xsl:if>
            <xsl:if test="Улица">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Улица (проспект, переулок и т.п.)</td>
                    <td><xsl:value-of select="Улица/@ТипУлица"/>&#160;<xsl:value-of select="Улица/@НаимУлица"/></td>
                </tr>
                
            </xsl:if>
            <xsl:if test="@Дом">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Дом (владение и т.п.)</td>
                    <td><xsl:value-of select="@Дом"/></td>
                </tr>                
            </xsl:if>
            <xsl:if test="@Корпус">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Корпус (строение и т.п.)</td>
                    <td><xsl:value-of select="@Корпус"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="@Кварт">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Квартира (офис и т.п.)</td>
                    <td><xsl:value-of select="@Кварт"/></td>
                </tr>   
            </xsl:if>                   
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="СвОбрЮЛ">
            <tr>
                <td id="ObrUL" colspan="3" style="text-align:center"><b>Сведения о регистрации (образовании) юридического лица </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Способ образования юридического лица</td>
                <td><xsl:value-of select="СпОбрЮЛ/@КодСпОбрЮЛ"/> - <xsl:value-of select="СпОбрЮЛ/@НаимСпОбрЮЛ"/> </td>
            </tr>            
                <tr>
                    <td class="num" align="center"></td>
                    <td>Основной государственный регистрационный номер юридического лица</td>
                    <td><xsl:value-of select="@ОГРН"/></td>
                </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Дата присвоения ОГРН</td>
                <td><xsl:value-of select="@ДатаОГРН"/></td>
            </tr>
            <xsl:if test="@РегНом">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Регистрационный номер, присвоенный российскому юридическому лицу до 1 июля 2002 года, или регистрационный номер юридического лица на территории Республики Крым или территории города федерального значения Севастополя на день принятия в РФ и образования в составе РФ новых субъектов - Республики Крым и города федерального значения Севастополя</td>
                    <td><xsl:value-of select="@РегНом"/></td>
                </tr> 
            </xsl:if>
            <xsl:if test="@ДатаРег">
               <tr>
                   <td class="num" align="center"></td>
                   <td>Дата регистрации юридического лица до 1 июля 2002 года, а также в отношении ЮЛ зарегистрированных на территории Республики Крым или территории города федерального значения Севастополя на день принятия в РФ и образования в составе РФ новых субъектов - Республики Крым и города федерального значения Севастополя</td>
                   <td><xsl:value-of select="@ДатаРег"/></td>
               </tr>
            </xsl:if>
            <xsl:if test="@НаимРО">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Наименование органа, зарегистрировавшего юридическое лицо до 1 июля 2002 года, а также в отношении ЮЛ зарегистрированных на территории Республики Крым или территории города федерального значения Севастополя на день принятия в РФ и образования в составе РФ новых субъектов - Республики Крым и города федерального значения Севастополя </td>
                    <td><xsl:value-of select="@НаимРО"/></td>
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/> <p><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></p></td>
            </tr>
        </xsl:template>
        <xsl:template match="СпОбрЮЛ">   
                <tr>
                    <td class="num" align="center"></td>
                    <td>Код способа образования по справочнику СЮЛНД</td>
                    <td><xsl:value-of select="@КодСпОбрЮЛ"/></td>
                </tr>
                <tr>
                    <td class="num" align="center"></td>
                    <td>Наименование способа образования юридического лица</td>
                    <td><xsl:value-of select="@НаимСпОбрЮЛ"/></td>
                </tr>
            </xsl:template>
        <xsl:template match="СвРегОрг">            
            <tr>
                <td class="num" align="center"></td>
                <td>Код органа по справочнику СОУН</td>
                <td><xsl:value-of select="@КодНО"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td id="SvRegOrg">Наименование регистрирующего (налогового) органа</td>
                <td><xsl:value-of select="@НаимНО"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Адрес регистрирующего органа</td>
                <td><xsl:value-of select="@АдрРО"/></td>
            </tr> 
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/> <br/> <xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template name="СвСтатус">
            <tr>
                <td id="SvStatus" colspan="3" style="text-align:center"><b>Сведения о состоянии (статусе) юридического лица</b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения о правоспособности (статусе) юридического лица</td>
                <td><xsl:value-of select="СвСтатус/@КодСтатусЮЛ"/> - <xsl:value-of select="СвСтатус/@НаимСтатусЮЛ"/></td>
            </tr>
            <xsl:if test="СвРешИсклЮЛ">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения о решении о предстоящем исключении недействующего ЮЛ из ЕГРЮЛ и его публикации </td>
                    <td>Решение № <xsl:value-of select="СвРешИсклЮЛ/@НомерРеш"/> от - <xsl:value-of select="СвРешИсклЮЛ/@ДатаРеш"/>
                        <br/>Опубликовно <xsl:value-of select="СвРешИсклЮЛ/@ДатаПубликации"/> в № <xsl:value-of select="СвРешИсклЮЛ/@НомерЖурнала"/> 
                    </td>
                </tr>
            </xsl:if>            
        </xsl:template>
        <xsl:template match="СвПрекрЮЛ">
            <tr>
                <td id="SvPrekUl" colspan="3" style="text-align:center"><b>Сведения о прекращении юридического лица</b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Способ прекращения юридического лица</td>
                <td><xsl:value-of select="СпПрекрЮЛ/@КодСпПрекрЮЛ"/>  - <xsl:value-of select="СпПрекрЮЛ/@НаимСпПрекрЮЛ"/>
                    <xsl:if test="СвРешИсклЮЛ">
                        <br/> Опубликовно <xsl:value-of select="СвРешИсклЮЛ/@ДатаПубликации"/> в № <xsl:value-of select="СвРешИсклЮЛ/@НомерЖурнала"/> 
                    </xsl:if>                    
                </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Дата прекращения юридического лица</td>
                <td><xsl:value-of select="@ДатаПрекрЮЛ"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения о регистрирующем (налоговом) органе, внесшем запись о прекращении юридического лица</td>
                <td><xsl:value-of select="СвРегОрг/@КодНО"/> - <xsl:value-of select="СвРегОрг/@НаимНО"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/> <xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="СвАдрЭлПочты">
            <tr>
                <td id = "Email" colspan="3" style="text-align:center"><b>Сведения об адресе электронной почты юридического лица</b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td><p style="text-align:left">Адрес электронной почты</p></td>
                <td><p style="text-align:left"><xsl:value-of select="@E-mail"/></p></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td><p style="text-align:left">ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</p></td>
                <td><p style="text-align:left"><xsl:value-of select="ГРНДата/@ГРН"/></p> <p><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></p></td>
            </tr> 
        </xsl:template>
        <xsl:template match="СвУчетНО">
            <tr>
                <td id ="SvUchN" colspan="3" style="text-align:center"><b>Сведения об учете в налоговом органе</b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ИНН</td>
                <td><xsl:value-of select="@ИНН"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>КПП</td>
                <td><xsl:value-of select="@КПП"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Дата постановки на учет в налоговом органе</td>
                <td><xsl:value-of select="@ДатаПостУч"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения о налоговом органе, в котором юридическое лицо состоит (для ЮЛ, прекративших деятельность - состояло) на учете</td>
                <td><xsl:value-of select="СвНО/@КодНО"/> - <xsl:value-of select="СвНО/@НаимНО"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/> <xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>           
        </xsl:template>
        <xsl:template match="СвРегПФ">
            <tr>
                <td id="SvRegPF" colspan="3" style="text-align:center"><b>Сведения о регистрации юридического лица в качестве страхователя в территориальном органе Пенсионного фонда Российской Федерации </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Регистрационный номер в территориальном органе Пенсионного фонда Российской Федерации</td>
                <td><p style="text-align:left"><xsl:value-of select="@РегНомПФ"/></p></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Дата регистрации юридического лица в качестве страхователя</td>
                <td><xsl:value-of select="@ДатаРег"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения о территориальном органе Пенсионного фонда Российской </td>
                <td><xsl:value-of select="СвОргПФ/@КодПФ"/> - <xsl:value-of select="СвОргПФ/@НаимПФ"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="СвРегФСС">
            <tr>
                <td id="SvRegFSS" colspan="3" style="text-align:center"><b>Сведения о регистрации юридического лица в качестве страхователя в исполнительном органе Фонда социального страхования Российской Федерации </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Регистрационный номер в исполнительном органе Фонда социального страхования Российской Федерации</td>
                <td><xsl:value-of select="@РегНомФСС"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Дата регистрации юридического лица в качестве страхователя</td>
                <td><xsl:value-of select="@ДатаРег"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения об исполнительном органе Фонда социального страхования Российской Федерации</td>
                <td><xsl:value-of select="СвОргФСС/@КодФСС"/> - <xsl:value-of select="СвОргФСС/@НаимФСС"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="СвУстКап">
            <tr>
                <td id="SvUstKap" colspan="3" style="text-align:center"><b>Сведения о размере указанного в учредительных документах коммерческой организации уставного капитала (складочного капитала, уставного фонда, паевого фонда) </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Наименование вида капитала</td>
                <td><xsl:value-of select="@НаимВидКап"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Размер в рублях</td>
                <td><xsl:value-of select="@СумКап"/></td>
            </tr>
            <xsl:if test="ДоляРубля">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Доля рубля в капитале</td>
                    <td><xsl:value-of select="ДоляРубля/@Числит"/>/<xsl:value-of select="ДоляРубля/@Знаменат"/></td>
                </tr>
                
            </xsl:if>
            <xsl:if test="СведУмУК">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения о нахождении хозяйственного общества в процессе уменьшения уставного капитала</td>
                    <td>Уменьшение на <xsl:value-of select="СведУмУК/@СведУмУК"/> по решению от /<xsl:value-of select="СведУмУК/@ДатаРеш"/></td>
                </tr>
            </xsl:if>            
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="СвТипУстКап">
            <tr>
                <td id="SvTipUS" colspan="3" style="text-align:center"><b>Сведения об использовании юридическим лицом типового устава </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения о нормативном правовом акте об утверждении типового устава</td>
                <td><xsl:value-of select="@СвНПАУтвТУ"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="ДоляУстКап">
            <tr>
                <td colspan="3" style="text-align:center">Доля в уставном капитале (складочном капитале, уставном фонде, паевом фонде), внесенная в ЕГРЮЛ </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Номинальная стоимость доли в рублях</td>
                <td><xsl:value-of select="@НоминСтоим"/></td>
            </tr>
            
            <xsl:apply-templates select="РазмерДоли"/>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="РазмерДоли">
            <tr>
                <td class="num" align="center"></td>
                <td>Размер доли (в процентах или в виде дроби - десятичной или простой) </td>
                <td>
                    <xsl:if test="Процент">
                        <xsl:value-of select="Процент"/>
                    </xsl:if>
                    <xsl:if test="@ДробДесят">
                        <xsl:value-of select="ДробДесят"/>
                    </xsl:if>
                    <xsl:if test="@ДробПрост">
                        <xsl:value-of select="ДробПрост/@Числит"/> / <xsl:value-of select="РазмерДоли/ДробПрост/@Знаменат"/>
                    </xsl:if>
                </td> 
            </tr>
        </xsl:template>
        <xsl:template name="СвУпрОрг">            
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>            
            <tr>
                <td colspan="3" style="text-align:center">Сведения о наименовании и (при наличии) ОГРН и ИНН ЮЛ - управляющей организации</td>
            </tr>
            <xsl:apply-templates select="НаимИННЮЛ"/>
            <xsl:if test="СвРегИн">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о регистрации иностранного ЮЛ в стране происхождения, внесенные в ЕГРЮЛ </td>
                </tr>
                <xsl:apply-templates select="СвРегИн"/>
            </xsl:if>
            <xsl:if test="СвНедДанУпрОрг">
                <tr>
                    <td colspan="3" style="text-align:center"></td>
                </tr>
                <xsl:for-each select="СвНедДанУпрОрг">
                    <xsl:call-template name="СвНедДанУпрОрг"/>                             
                </xsl:for-each>
            </xsl:if>
            <xsl:if test="СвРегИн">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о наименовании представительства или филиала в Российской Федерации, через которое иностранное ЮЛ осуществляет полномочия управляющей организации</td>
                </tr> 
                    <xsl:apply-templates select="СвПредЮЛ"/>
            </xsl:if>
            <xsl:if test="СвАдрРФ">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения об адресе управляющей организации в Российской Федерации</td>
                </tr> 
                <xsl:apply-templates select="СвАдрРФ"/>
            </xsl:if>
            <xsl:if test="СвНомТел">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о контактном телефоне</td>
                <xsl:apply-templates select="СвНомТел"/>
                </tr>
            </xsl:if>
            <xsl:if test="ПредИнЮЛ">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о лице, через которое иностранное юридическое лицо осуществляет полномочия управляющей организации</td>
                    <xsl:apply-templates select="ПредИнЮЛ"/>
                </tr>
            </xsl:if>
            
        </xsl:template>
        <xsl:template match="НаимИННЮЛ">
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
            <tr>
                <td class="num" align="center"></td>
                <td>Основной государственный регистрационный номер юридического лица</td>
                <td><p style="text-align:left"><xsl:value-of select="@ОГРН"/></p></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ИНН юридического лица</td>
                <td><xsl:value-of select="@ИНН"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Полное наименование юридического лица</td>
                <td><xsl:value-of select="@НаимЮЛПолн"/></td>
            </tr>
            
            
        </xsl:template>
        <xsl:template match="СвРегИн">
            <tr>
                <td class="num" align="center"></td>
                <td>Код страны происхождения</td>
                <td><xsl:value-of select="@ОКСМ"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Наименование страны происхождения</td>
                <td><xsl:value-of select="@НаимСтран"/></td>
            </tr>
            <xsl:if test="@ДатаРег">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Дата регистрации</td>
                    <td><xsl:value-of select="@ДатаРег"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="@РегНомер">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Регистрационный номер</td>
                    <td><xsl:value-of select="@РегНомер"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="@НаимРегОрг">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Наименование регистрирующего органа</td>
                    <td><xsl:value-of select="@НаимРегОрг"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="@АдрСтр">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Адрес (место нахождения) в стране происхождения</td>
                    <td><xsl:value-of select="@АдрСтр"/></td>
                </tr>   
            </xsl:if>
                     
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="СведДолжнФЛ">
            <tr>
                <td colspan="3" style="text-align:center"></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
            </tr>             
            <xsl:apply-templates select="СвФЛ"/>
            <xsl:apply-templates select="СвДолжн"/>    
            <xsl:if test="СвНомТел">
                 <xsl:apply-templates select="СвНомТел"/>
            </xsl:if>           
            <xsl:if test="СвНедДанДолжнФЛ">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о недостоверности данных о лице, имеющем право без доверенности действовать от имени юридического лица </td>
                </tr>
                <xsl:apply-templates select="СвНедДанДолжнФЛ"/> 
            </xsl:if>
            <!---ПД -->
            <xsl:if test="СвРождФЛ">
                <xsl:apply-templates select="СвРождФЛ"/>
            </xsl:if>
            <xsl:if test="УдЛичнФЛ">
                <xsl:apply-templates select="УдЛичнФЛ"/>
            </xsl:if>
            <xsl:if test="АдресМЖРФ">
                <xsl:apply-templates select="АдресМЖРФ"/>
            </xsl:if>
            <xsl:if test="АдрМЖИн">
                <xsl:apply-templates select="АдрМЖИн"/>
            </xsl:if>
            <xsl:if test="СвДискв">
                <tr>
                    <td colspan="3" style="text-align:center"></td>
                </tr>
                <xsl:for-each select="СвДискв">
                    <xsl:call-template name="СвДискв"/>                             
                </xsl:for-each>
            </xsl:if>
            
        </xsl:template>
        <xsl:template match="СвДолжн">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о должности ФЛ </td>
            </tr>
            <xsl:if test="ОГРНИП">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ОГРНИП</td>
                    <td><xsl:value-of select="@ОГРНИП"/></td>
                </tr>
            </xsl:if>
            
            <tr>
                <td class="num" align="center"></td>
                <td>Вид должностного лица по справочнику СКФЛЮЛ </td>
                <td><xsl:value-of select="@ВидДолжн"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Наименование вида должностного лица по справочнику СКФЛЮЛ </td>
                <td><xsl:value-of select="@НаимВидДолжн"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Наименование должности</td>
                <td><xsl:value-of select="@НаимДолжн"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td align="left"><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>
        </xsl:template>
        <xsl:template match="СвФЛ">
            <tr>
                <td class="num" align="center"></td>
                <td>Фамилия</td>
                <td><xsl:value-of select="@Фамилия"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Имя</td>
                <td><xsl:value-of select="@Имя"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Отчество</td>
                <td><xsl:value-of select="@Отчество"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ИНН</td>
                <td><xsl:value-of select="@ИННФЛ"/></td>
            </tr>  
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="СвНомТел">
            <tr>
                <td class="num" align="center"></td>
                <td>Контактный телефон</td>
                <td><xsl:value-of select="@НомТел"/></td>
            </tr>
            <tr>
                <td class="num" align="center"><p style="text-align:center"></p></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template name="СвУчредит">
            <xsl:for-each select="УчрЮЛРос">
                <xsl:call-template name="УчрЮЛРос"/>                
            </xsl:for-each>
            <xsl:for-each select="УчрЮЛИн">
                <xsl:call-template name="УчрЮЛИн"/>                
            </xsl:for-each>
            <xsl:for-each select="УчрФЛ">
                <xsl:call-template name="УчрФЛ"/>                
            </xsl:for-each>
            <xsl:for-each select="УчрРФСубМО">
                <xsl:call-template name="УчрРФСубМО"/>
            </xsl:for-each>
            <xsl:for-each select="УчрПИФ">                               
                <xsl:call-template name="УчрПИФ"/>
            </xsl:for-each>
            
        </xsl:template>
        <xsl:template name="УчрЮЛИн">
            <tr>
                <td colspan="3" style="text-align:center">Сведения об учредителе (участнике) - иностранном юридическом лице </td>
            </tr>
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                        <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                        <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="НаимИННЮЛ"/>
            <xsl:if test="СвРегИн">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о регистрации в стране происхождения </td>
                </tr>
                <xsl:apply-templates select="СвРегИн"/>
            </xsl:if>
            <xsl:for-each select="СвНедДанУчр">
                <xsl:call-template name="СвНедДанУчр">                               
                </xsl:call-template>
            </xsl:for-each>
            <xsl:if test="ДоляУстКап">
                <xsl:apply-templates select="ДоляУстКап"/> 
            </xsl:if>
            <xsl:for-each select="СвОбрем">
                <xsl:call-template name="СвОбрем"/>                
            </xsl:for-each>           
        </xsl:template>
        <xsl:template name="УчрФЛ">
            <tr>
                <td colspan="3" style="text-align:center">Сведения об учредителе (участнике) - физическом лице </td>
            </tr>
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>            
            <xsl:apply-templates select="СвФЛ"/>
            <xsl:for-each select="СвНедДанУчр">
                <xsl:call-template name="СвНедДанУчр"/>                
            </xsl:for-each>
            <xsl:if test="СвРождФЛ"> 
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о рождении ФЛ </td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="СвРождФЛ"/>            
            <xsl:apply-templates select="УдЛичнФЛ"/>
            <xsl:apply-templates select="АдресМЖРФ"/>
            <xsl:apply-templates select="АдрМЖИн"/>
            <xsl:apply-templates select="ДоляУстКап"/>           
            <xsl:for-each select="СвОбрем">
                <xsl:call-template name="СвОбрем">                               
                </xsl:call-template>
            </xsl:for-each>
            <xsl:apply-templates select="СвДовУпрЮЛ"/> 
            <xsl:apply-templates select="СвДовУпрФЛ"/> 
            <xsl:apply-templates select="ЛицоУпрНасл"/>
        </xsl:template>
        <xsl:template name="УчрРФСубМО">
            <tr>
                <td colspan="3" style="text-align:center">Сведения об учредителе (участнике) - Российской Федерации, субъекте Российской Федерации, муниципальном образовании</td>
            </tr>
            <xsl:apply-templates select="ВидНаимУчр"/>
            <xsl:for-each select="СвНедДанУчр">
                <xsl:call-template name="СвНедДанУчр">                               
                </xsl:call-template>
            </xsl:for-each>
            <xsl:apply-templates select="ДоляУстКап"/>           
            <xsl:for-each select="СвОргОсущПр">
                <xsl:call-template name="СвОргОсущПр"/>
            </xsl:for-each>
            <xsl:for-each select="СвФЛОсущПр">
                <xsl:call-template name="СвФЛОсущПр"/>
            </xsl:for-each>
            <xsl:for-each select="СвОбрем">
                <xsl:call-template name="СвОбрем"/>
            </xsl:for-each>            
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>            
        </xsl:template>
        <xsl:template name="УчрЮЛРос">
            <tr>
                <td colspan="3" style="text-align:center">Сведения об учредителе (участнике) - российском юридическом лице </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
            </tr>
            <xsl:apply-templates select="НаимИННЮЛ"/>
            <xsl:if test="СвРегСтарые">
                <xsl:apply-templates select="СвРегСтарые"/>
            </xsl:if>
            <xsl:for-each select="СвНедДанУчр">
                <xsl:call-template name="СвНедДанУчр"/>
            </xsl:for-each>
                <xsl:apply-templates select="ДоляУстКап"/>
            <xsl:for-each select="СвОбрем">
                <xsl:call-template name="СвОбрем"/>
            </xsl:for-each>
        </xsl:template>
        <xsl:template name="СвОбрем">
            <tr>
                <td colspan="3" style="text-align:center">Сведения об обременении доли участника, внесенные в ЕГРЮЛ </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Вид обременения</td>
                <td><xsl:value-of select="@ВидОбрем"/></td>
            </tr>
            <xsl:if test="@СрокОбременения">
                <tr>
                <td class="num" align="center"></td>
                <td>Срок обременения или порядок определения срока</td>
                <td><xsl:value-of select="@СрокОбременения"/></td>
            </tr>
                </xsl:if>
            <xsl:if test="РешСуд">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения о решении судебного органа, по которому на долю учредителя (участника) наложено обременение</td>
                    <td><xsl:value-of select="РешСуд/@КНаимСуда"/> <br/>
                        Решение №<xsl:value-of select="РешСуд/@Номер"/> от <xsl:value-of select="РешСуд/@Дата"/>
                    </td>              
                </tr>
            </xsl:if>
            <xsl:if test="СвЗалогДержФЛ">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о залогодержателе - ФЛ </td>
                </tr>
            </xsl:if> 
            <xsl:if test="СвЗалогДержЮЛ">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о залогодержателе - ФЛ </td>
                </tr>
            </xsl:if>           
            <tr>
                <td class="num" align="center"></td>
                <td align="left">ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td align="left"><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>
            
        </xsl:template>
        <xsl:template name="СвРегСтарые">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о регистрации учредителя (участника) до 01.07.2002 г</td>
            </tr>
            <xsl:if test="РегНом">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Регистрационный номер, присвоенный юридическому лицу до 1 июля 2002 года</td>
                    <td><xsl:value-of select="@РегНом"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="ДатаРег">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Дата регистрации юридического лица до 1 июля 2002 года</td>
                    <td><xsl:value-of select="@ДатаРег"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="НаимРО">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Наименование органа, зарегистрировавшего юридическое лицо до 1 июля 2002 года</td>
                    <td><xsl:value-of select="@НаимРО"/></td>
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template name="СвОргОсущПр">
            <xsl:apply-templates select="НаимИННЮЛ"/>            
        </xsl:template>
        <xsl:template name="СвФЛОсущПр">
        <xsl:apply-templates select="СвФЛ"/>
        <xsl:apply-templates select="СвРождФЛ"/>
        <xsl:apply-templates select="УдЛичнФЛ"/>
        <xsl:apply-templates select="АдресМЖРФ"/>
        <xsl:apply-templates select="АдрМЖИн"/>
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>   
        </xsl:template>
        <xsl:template name="СвНаимПИФ">
            <tr>
                <td class="num" align="center"></td>
                <td>Название (индивидуальное обозначение) паевого инвестиционного фонда</td>
                <td><xsl:value-of select="@НаимПИФ"/></td>
            </tr>        
            <xsl:if test="ГРНДата">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                    <td><xsl:value-of select="ГРНДата/@ГРН"/> <br/> <xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
                </tr>  
            </xsl:if>        
        </xsl:template>
        <xsl:template name="СвУпрКомпПИФ">
            <tr>
                <td class="num" align="center"></td>
                <td>Наименование и (при наличии) ОГРН и ИНН управляющей компании паевого инвестиционного фонда</td>
                <td><xsl:value-of select="@УпрКомпПиф"/></td>
            </tr>        
            <xsl:if test="ГРНДата">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/> <br/> <xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>  
            </xsl:if>
        </xsl:template>
        <xsl:template name="ВидНаимУчр">
            <tr>
               <td class="num" align="center"></td>
               <td>Код вида учредителя</td>
                <td><xsl:value-of select="@КодУчрРФСубМО"/></td>
             </tr>
             <xsl:if test="@НаимМО">
                 <tr>
                     <td class="num" align="center"></td>
                     <td>Наименование муниципального образования</td>
                     <td><xsl:value-of select="@НаимМО"/></td>
                 </tr>
                </xsl:if>
                <xsl:if test="@НаимМО">
                    <tr>
                        <td class="num" align="center"></td>
                        <td>Код субъекта Российской Федерации, который является учредителем (участником) юридического лица или на территории которого находится муниципальное образование, которое является учредителем (участником) юридического лица</td>
                        <td><xsl:value-of select="@КодРегион"/></td>
                    </tr>
                </xsl:if>
                <xsl:if test="@НаимМО">
                    <tr>
                        <td class="num" align="center"></td>
                        <td>Наименование субъекта Российской Федерации</td>
                        <td><xsl:value-of select="@НаимРегион"/></td>
                    </tr>
                </xsl:if>
            </xsl:template>
        <xsl:template name="УчрПИФ">
             <tr>
                 <td colspan="3" style="text-align:center">Сведения о паевом инвестиционном фонде, в состав имущества которого включена доля в уставном капитале  </td>
             </tr>
             <xsl:apply-templates select="СвНаимПИФ"/>
             <xsl:for-each select="СвНедДанУчр">
                <xsl:call-template name="СвНедДанУчр"/>
             </xsl:for-each>    
                
             <xsl:if test="ГРНДатаПерв">
               <tr>
                   <td><p style="text-align:center"></p></td>
                   <td><p style="text-align:left">ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</p></td>
                   <td><p style="text-align:left"><xsl:value-of select="ГРНДатаПерв/@ГРН"/></p> <p><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></p></td>
               </tr>
             </xsl:if>
             <xsl:apply-templates select="СвУпрКомпПИФ"/>
             <xsl:apply-templates select="ДоляУстКап"/>
             <xsl:for-each select="СвОбрем">
                 <xsl:call-template name="СвОбрем"/>
             </xsl:for-each>
        </xsl:template>
        <xsl:template match="СвДоляООО">
            <tr>
                <td id="SvDolOOO" colspan="3" style="text-align:center"><b>Сведения о доле в уставном капитале общества с ограниченной ответственностью, принадлежащей обществу  </b> </td>
            </tr>
            <xsl:apply-templates select="ДоляУстКап"/>
            <xsl:if test="@НоминСтоим">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Номинальная стоимость доли в рублях</td>
                    <td><xsl:value-of select="@НоминСтоим"/></td>
                </tr>
            </xsl:if>            
            <xsl:apply-templates select="РазмерДоли"/>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="СвДержРеестрАО">
            <tr>
                <td id="SvDerjReestrAO" colspan="3" style="text-align:center"><b>Сведения о держателе реестра акционеров акционерного общества </b> </td>
            </tr>
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="ДержРеестрАО"/>                
            
        </xsl:template>
        <xsl:template match="ДержРеестрАО">
            <xsl:if test="@ОГРН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Основной государственный регистрационный номер юридического лица</td>
                    <td><xsl:value-of select="@ОГРН"/></td>                
                </tr> 
            </xsl:if>
            <xsl:if test="@ИНН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ИНН юридического лица</td>
                    <td><xsl:value-of select="@ИНН"/></td>                
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>Полное наименование юридического лица</td>
                <td><xsl:value-of select="@НаимЮЛПолн"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="СвЛицензия">            
            <tr>
                <td class="num" align="center"></td>
                <td>Серия и номер лицензии</td>
                <td><xsl:value-of select="@НомЛиц"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Дата лицензии</td>
                <td><xsl:value-of select="@ДатаЛиц"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Дата начала действия лицензии</td>
                <td><xsl:value-of select="@ДатаНачЛиц"/></td>
            </tr>
            <xsl:if test="@ДатаОкончЛиц">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Дата окончания действия лицензии</td>
                    <td><xsl:value-of select="@ДатаОкончЛиц"/></td>
                </tr>
            </xsl:if>            
            <tr>
                <td class="num" align="center"></td>
                <td>Наименование лицензируемого вида деятельности, на который выдана лицензия</td>
                <td><xsl:value-of select="НаимЛицВидДеят"/>, </td>
                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения об адресе места осуществления лицензируемого вида деятельности</td>
                <xsl:if test="НаимЛицВидДеят">
                    <td><xsl:value-of select="МестоДейстЛиц"/>, </td>
                </xsl:if>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Наименование лицензирующего органа, выдавшего или переоформившего лицензию</td>
                <td><xsl:value-of select="ЛицОргВыдЛиц"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>
            <xsl:if test="СвПриостЛиц">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения о приостановлении действия лицензии</td>
                    <td><xsl:value-of select="СвПриостЛиц/@ДатаПриостЛиц"/> <p><xsl:value-of select="СвПриостЛиц/@ЛицОргПриостЛиц"/></p></td>
            </tr>
            </xsl:if>
            
        </xsl:template>
        <xsl:template name="СвРеорг">
            <xsl:apply-templates select="СвСтатус"/>
            <tr>
                <td id="SvReorg" colspan="3" style="text-align:center"><b>Сведения об участии в реорганизации</b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей сведения о начале реорганизации</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>
            <xsl:for-each select="ГРНДатаИзмСостРеоргЮЛ">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения записи, которой в ЕГРЮЛ внесены сведения об изменении состава участвующих в реорганизации юридических лиц </td>
                    <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
                </tr>
            </xsl:for-each>
            <xsl:for-each select="СвРеоргЮЛ">
                <xsl:call-template name="СвРеоргЮЛ"/>
            </xsl:for-each>
        </xsl:template>
        <xsl:template name="СвРеоргЮЛ">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о юридических лицах, участвующих в реорганизации</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Основной государственный регистрационный номер юридического лица</td>
                <td><xsl:value-of select="@ОГРН"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Полное наименование юридического лица</td>
                <td><xsl:value-of select="@НаимЮЛПолн"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ИНН юридического лица</td>
                <td><xsl:value-of select="@ИНН"/></td>
            </tr>
            <xsl:if test="СостЮЛпосле">
               <tr>
                   <td class="num" align="center"></td>
                   <td>Состояние юридического лица после завершения реорганизации</td>
                   <td><xsl:value-of select="@СостЮЛпосле"/></td>
               </tr>
            </xsl:if>
        </xsl:template>
        <xsl:template name="СвПредш">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о правопредшественнике </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Основной государственный регистрационный номер юридического лица</td>
                <td><xsl:value-of select="@ОГРН"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ИНН юридического лица</td>
                <td><xsl:value-of select="@ИНН"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Полное наименование юридического лица</td>
                <td><xsl:value-of select="@НаимЮЛПолн"/></td>
            </tr>
            <xsl:apply-templates select="СвЮЛсложнРеорг"/>            
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>
        </xsl:template>
        <xsl:template match="СвЮЛсложнРеорг">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о ЮЛ, путем реорганизации которого был создан правопредшественник при реорганизации в форме выделения или разделения с одновременным присоединением или слиянием</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Основной государственный регистрационный номер юридического лица</td>
                <td><xsl:value-of select="@ОГРН"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Полное наименование юридического лица</td>
                <td><xsl:value-of select="@НаимЮЛПолн"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ИНН юридического лица</td>
                <td><xsl:value-of select="@ИНН"/></td>
            </tr>
            
        </xsl:template>
        <xsl:template name="СвКФХПредш">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о крестьянском (фермерском) хозяйстве, на базе имущества которого создано юридическое лицо </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ОГРНИП крестьянского (фермерского) хозяйства</td>
                <td><xsl:value-of select="@ОГРНИП"/></td>
            </tr>
            <xsl:apply-templates select="СвФЛ"/>
        </xsl:template>
        <xsl:template name="СвКФХПреем">
            <tr>
                <td id="SvKFHPreem" colspan="3" style="text-align:center"><b>Сведения о крестьянском (фермерском) хозяйстве, которые внесены в ЕГРИП в связи с приведением правового статуса крестьянского (фермерского) хозяйства в соответствие с нормами части первой Гражданского кодекса Российской Федерации </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ОГРНИП крестьянского (фермерского) хозяйства</td>
                <td><xsl:value-of select="@ОГРНИП"/></td>
            </tr>
            <xsl:apply-templates select="СвФЛ"/>
        </xsl:template>
        <xsl:template name="СвПреем">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о правопреемнике </td>
            </tr>            
            <tr>
                <td class="num" align="center"></td>
                <td>Основной государственный регистрационный номер юридического лица</td>
                <td><xsl:value-of select="@ОГРН"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Полное наименование юридического лица</td>
                <td><xsl:value-of select="@НаимЮЛПолн"/></td>
            </tr>
            <xsl:if test="@ИНН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ИНН юридического лица</td>
                    <td><xsl:value-of select="@ИНН"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="СвЮЛсложнРеорг"/>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="СвЮЛсложнРеорг">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о ЮЛ, которое было создано в форме слияния с участием правопреемника, или к которому присоединился правопреемник при реорганизации в форме выделения или разделения с одновременным присоединением или слиянием</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Основной государственный регистрационный номер юридического лица</td>
                <td><xsl:value-of select="@ОГРН"/></td>
            </tr>            
            <xsl:if test="@ИНН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ИНН юридического лица</td>
                    <td><xsl:value-of select="@ИНН"/></td>
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>Полное наименование юридического лица</td>
                <td><xsl:value-of select="@НаимЮЛПолн"/></td>
            </tr>
        </xsl:template>
        <xsl:template name="СвЗапЕГРЮЛ">
            <tr>
                <td colspan="3" style="text-align:center"><b><xsl:value-of select="position()"/></b> </td>
            </tr>           
            <tr>
                <td class="num" align="center"></td>
                <td>Государственный регистрационный номер записи</td>
                <td><xsl:value-of select="@ГРН"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Дата внесения записи в ЕГРЮЛ</td>
                <td><xsl:value-of select="@ДатаЗап"/></td>
            </tr> 
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения о причине внесения записи в ЕГРЮЛ</td>
                <td><xsl:value-of select="ВидЗап/@КодСПВЗ"/> - <xsl:value-of select="ВидЗап/@НаимВидЗап"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения о регистрирующем (налоговом) органе, внесшем запись о прекращении юридического лица</td>
                <td><xsl:value-of select="СвРегОрг/@КодНО"/> - <xsl:value-of select="СвРегОрг/@НаимНО"/></td>
            </tr>
            <xsl:for-each select="СвЗаявФЛ">
                <xsl:call-template name="СвЗаявФЛ"/>   
            </xsl:for-each>
            <xsl:if test="СведПредДок">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о документах, представленных при внесении записи в ЕГРЮЛ</td>
                </tr>
                <xsl:for-each select="СведПредДок">                
                    <xsl:call-template name="СведПредДок"/>   
                </xsl:for-each>    
            </xsl:if>           
            <xsl:for-each select="СвСвид">
                <xsl:call-template name="СвСвид"/>   
            </xsl:for-each>
            <xsl:if test="ГРНДатаИспрПред/@ГРН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата записи, в которую внесены исправления</td>
                    <td><xsl:value-of select="ГРНДатаИспрПред/@ГРН"/> от <xsl:value-of select="ГРНДатаИспрПред/@ДатаЗап"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="ГРНДатаНедПред/@ГРН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата записи, которая признана недействительной</td>
                    <td><xsl:value-of select="ГРНДатаНедПред/@ГРН"/> от <xsl:value-of select="ГРНДатаНедПред/@ДатаЗап"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="СвСтатусЗап"/>
        </xsl:template>
        <xsl:template match="СвСтатусЗап">
            <xsl:if test="ГРНДатаНед/@ГРН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения записи, которой запись признана недействительной</td>
                    <td><xsl:value-of select="ГРНДатаНед/@ГРН"/> от <xsl:value-of select="ГРНДатаНед/@ДатаЗап"/></td>
                </tr>                
            </xsl:if> 
            <xsl:for-each select="ГРНДатаИспр">                
                <xsl:call-template name="ГРНДатаИспр"/>
            </xsl:for-each>
        </xsl:template>
        <xsl:template name="ГРНДатаИспр">
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата записи, которой внесены исправления в связи с технической ошибкой</td>
                <td><xsl:value-of select="@ГРН"/> от <xsl:value-of select="@ДатаЗап"/></td>
            </tr>     
        </xsl:template>
        <xsl:template name="СвЗаявФЛ">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о заявителе </td>
            </tr>
            <xsl:if test="ВидЗаяв/@НаимСЗОЮЛ">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Заявитель</td>
                    <td><xsl:value-of select="ВидЗаяв/@КодСЗОЮЛ"/> - <xsl:value-of select="ВидЗаяв/@НаимСЗОЮЛ"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="СвЮЛ/@ОГРН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения о юридическом лице, от имени которого действует заявитель</td>
                    <td><xsl:value-of select="СвЮЛ/@ОГРН"/>/<xsl:value-of select="СвЮЛ/@ИНН"/> - <xsl:value-of select="СвЮЛ/@НаимЮЛПолн"/></td>
            </tr>
            </xsl:if>
            <xsl:if test="СвУпрОрг/@ОГРН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения об управляющей компании</td>
                    <td><xsl:value-of select="СвУпрОрг/@ОГРН"/>/<xsl:value-of select="СвУпрОрг/@ИНН"/> - <xsl:value-of select="СвУпрОрг/@НаимЮЛПолн"/></td>
            </tr>
            </xsl:if>
            <xsl:if test="СвФЛ/СвФИОИНН/@Фамилия">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения о ФЛ - заявителе</td>
                    <td><xsl:value-of select="СвФЛ/СвФИОИНН/@Фамилия"/> <xsl:value-of select="СвФЛ/СвФИОИНН/@Имя"/> <xsl:value-of select="СвФЛ/СвФИОИНН/@Отчество"/>
                        <xsl:value-of select="СвФЛ/СвФИОИНН/@ИННФЛ"/></td>
                </tr>    
            </xsl:if>
                        
        </xsl:template>
        <xsl:template name="СведПредДок">
            <tr>
                <td colspan="3" style="text-align:center"></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
               <td>Наименование документа</td>
               <td><xsl:value-of select="НаимДок"/></td>
            </tr>
            <xsl:if test="НомДок">
                    <tr>
                       <td class="num" align="center"></td>
                       <td>Номер документа</td>
                       <td><xsl:value-of select="НомДок"/></td>
                   </tr> 
            </xsl:if>
            <xsl:if test="ДатаДок">
                    <tr>
                        <td class="num" align="center"></td>
                        <td>Дата документа</td>
                        <td><xsl:value-of select="ДатаДок"/></td>
                    </tr> 
            </xsl:if>            
        </xsl:template>
        <xsl:template name="СвСвид">
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения о свидетельстве, подтверждающем факт внесения записи в ЕГРЮЛ </td>
                <td><xsl:value-of select="@Серия"/>&#160;<xsl:value-of select="@Номер"/> от <xsl:value-of select="@ДатаВыдСвид"/></td>
            </tr> 
            <xsl:if test="ГРНДатаСвидНед/@ГРН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                    <td><xsl:value-of select="ГРНДатаСвидНед/@ГРН"/><br/><xsl:value-of select="ГРНДатаСвидНед/@ДатаЗаписи"/></td>
                </tr> 
            </xsl:if>
            
        </xsl:template>
        <xsl:template name="СвОКВЭД">
            <tr>
                <td colspan="3" style="text-align:center"><b>Сведения об основном виде деятельности </b> </td>
            </tr>
            <xsl:if test="СвОКВЭДОсн">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Код и наименование вида деятельности</td>
                    <td><xsl:value-of select="СвОКВЭДОсн/@КодОКВЭД"/> - <xsl:value-of select="СвОКВЭДОсн/@НаимОКВЭД"/></td>
                </tr>
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                    <td><xsl:value-of select="СвОКВЭДОсн/ГРНДата/@ГРН"/><br/><xsl:value-of select="СвОКВЭДОсн/ГРНДата/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="СвОКВЭДДоп">
                <tr>
                    <td colspan="3" style="text-align:center"><b>Сведения о дополнительном виде деятельности </b> </td>
                </tr>
            <xsl:for-each select="СвОКВЭДДоп">
                <xsl:call-template name="СвОКВЭДДоп"/>   
            </xsl:for-each>
            </xsl:if>           
            
        </xsl:template>
        <xsl:template name="СвОКВЭДДоп">
            <tr>
                <td colspan="3" style="text-align:center"><xsl:value-of select="position()"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Код и наименование вида деятельности</td>
                <td><xsl:value-of select="@КодОКВЭД"/> - <xsl:value-of select="@НаимОКВЭД"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>
        </xsl:template>
        <xsl:template match="СвПодразд">
            <tr>
                <td id="SvPodrazd" colspan="3" style="text-align:center"><b>Сведения об обособленных подразделениях юридического лица </b> </td>
            </tr>
            <xsl:if test="СвФилиал">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о филиалах юридического лица</td>
                </tr>
                <xsl:for-each select="СвФилиал">
                    <xsl:call-template name="СвФилиал"/>                
                </xsl:for-each>
            </xsl:if>
            <xsl:if test="СвПредстав">
                <tr>
                    <td colspan="3" style="text-align:center">Сведения о представительствах юридического лица</td>
                </tr>
                <xsl:for-each select="СвПредстав">
                    <xsl:call-template name="СвПредстав"/>                
                </xsl:for-each>
            </xsl:if>
        </xsl:template>
        <xsl:template name="СвФилиал">
            <tr>
                <td colspan="3" style="text-align:center"><xsl:value-of select="position()"/></td>
            </tr>
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном филиале</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                 </tr>
            </xsl:if>
            <xsl:apply-templates select="СвНаим"/>
            <xsl:apply-templates select="АдрМНРФ"/>
            <xsl:apply-templates select="АдрМНИн"/>
            <xsl:apply-templates select="СвУчетНОФилиал"/>
        </xsl:template>
        <xsl:template name="СвПредстав">
            <tr>
                <td colspan="3" style="text-align:center"><xsl:value-of select="position()"/></td>
            </tr>
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном представительстве</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="СвНаим"/>
            <xsl:apply-templates select="АдрМНРФ"/>
            <xsl:apply-templates select="АдрМНИн"/>
            <xsl:apply-templates select="СвУчетНОПредстав"/>
        </xsl:template>
        <xsl:template match="СвНаим">
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Наименование</td>
                <td><xsl:value-of select="@НаимПолн"/></td>                
            </tr>
        </xsl:template>
        <xsl:template match="АдрМНРФ">
            <tr>
                <td colspan="3" style="text-align:center">Адрес (место расположения) на территории Российской Федерации</td>
            </tr>
            <xsl:if test="@Индекс">
                <tr>
                    <td class="num" align="center"></td>
                    <td align="left">Индекс</td>
                    <td align="left"><xsl:value-of select="@Индекс"/></td>
                </tr>   
            </xsl:if>             
            <tr>
                <td class="num" align="center"></td>
                <td align="left">Код субъекта Российской Федерации</td>
                <td align="left"><xsl:value-of select="@КодРегион"/> - <xsl:value-of select="Регион/@ТипРегион"/>&#160;<xsl:value-of select="Регион/@НаимРегион"/></td>
            </tr>
            <xsl:if test="@КодАдрКладр">
                <tr>
                    <td class="num" align="center"></td>
                    <td align="left">Код адреса по КЛАДР</td>
                    <td align="left"><xsl:value-of select="@КодАдрКладр"/></td>
                </tr> 
            </xsl:if>       
            <tr>
                <td class="num" align="center"></td>
                <td align="left">Город (волость и т.п.)</td>
                <td align="left"><xsl:value-of select="Город/@ТипГород"/>&#160;<xsl:value-of select="Город/@НаимГород"/></td>
            </tr>
            <xsl:if test="НаселПункт">
                <tr>
                    <td class="num" align="center"></td>
                    <td align="left">Населенный пункт (село и т.п.)</td>
                    <td align="left"><xsl:value-of select="НаселПункт/@ТипНаселПункт"/>&#160;<xsl:value-of select="НаселПункт/@НаимНаселПункт"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="Район">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Район (улус и т.п.)</td>
                    <td><xsl:value-of select="Район/@ТипРайон"/>&#160;<xsl:value-of select="Район/@НаимРайон"/></td>
                </tr>
                
            </xsl:if>
            <xsl:if test="Улица">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Улица (проспект, переулок и т.п.)</td>
                    <td><xsl:value-of select="Улица/@ТипУлица"/>&#160;<xsl:value-of select="Улица/@НаимУлица"/></td>
                </tr>
                
            </xsl:if>
            <xsl:if test="@Дом">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Дом (владение и т.п.)</td>
                    <td><xsl:value-of select="@Дом"/></td>
                </tr>                
            </xsl:if>
            <xsl:if test="@Корпус">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Корпус (строение и т.п.)</td>
                    <td><xsl:value-of select="@Корпус"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="@Кварт">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Квартира (офис и т.п.)</td>
                    <td><xsl:value-of select="@Кварт"/></td>
                </tr>   
            </xsl:if>            
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="АдрМНИн">
            <tr>
                <td colspan="3" style="text-align:center">Адрес (место расположения) за пределами территории Российской Федерации</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">Код страны</td>
                <td align="left"><xsl:value-of select="@ОКСМ"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">Наименование страны</td>
                <td align="left"><xsl:value-of select="@НаимСтран"/></td>
            </tr>
            <xsl:if test="@АдрИн">
                <tr>
                    <td class="num" align="center"></td>
                    <td align="left">Адрес</td>
                    <td align="left"><xsl:value-of select="@АдрИн"/></td>
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="СвУчетНОФилиал">
            <tr>
                <td colspan="3" style="text-align:center">Сведения об учете в налоговом органе по месту нахождения филиала</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">КПП филиала/представительства</td>
                <td align="left"><xsl:value-of select="@КПП"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">ДатаПостУч</td>
                <td align="left"><xsl:value-of select="@ДатаПостУч"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения о налоговом органе по месту нахождения филиала/представительства</td>
                <td><xsl:value-of select="СвНО/@КодНО"/> - <xsl:value-of select="СвНО/@НаимНО"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="СвУчетНОПредстав">
            <tr>
                <td colspan="3" style="text-align:center">Сведения об учете в налоговом органе по месту нахождения филиала</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">КПП филиала/представительства</td>
                <td align="left"><xsl:value-of select="@КПП"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">ДатаПостУч</td>
                <td align="left"><xsl:value-of select="@ДатаПостУч"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Сведения о налоговом органе по месту нахождения филиала/представительства</td>
                <td><xsl:value-of select="СвНО/@КодНО"/> - <xsl:value-of select="СвНО/@НаимНО"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr>  
        </xsl:template>        
        <xsl:template name="СвНедДанУпрОрг">
            <tr>
                <td colspan="3" style="text-align:center"></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td style="text-align:left">Признак недостоверности данных</td>
                <td><xsl:value-of select="@ПризнНедДанУпрОрг"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Текст о недостоверности сведений, выводимый в выписке в строке с наименованием "Дополнительные сведения"</td>
                <td><xsl:value-of select="@ТекстНедДанУпрОрг"/></td>                
            </tr>
            <xsl:if test="РешСудНедДанУпрОрг">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения о решении суда, на основании которого указанные сведения признаны недостоверными</td>
                    <td><xsl:value-of select="РешСудНедДанУпрОрг/@КНаимСуда"/> <br/>
                        Решение №<xsl:value-of select="РешСудНедДанУпрОрг/@Номер"/> от <xsl:value-of select="РешСудНедДанУпрОрг/@Дата"/>
                     </td>              
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="СвПредЮЛ">
            <tr>
                <td class="num" align="center"></td>
                <td>Полное наименование представительства или филиала в Российской Федерации, через которое иностранное ЮЛ осуществляет полномочия управляющей организации</td>
                <td><xsl:value-of select="@НаимПредЮЛ"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="ПредИнЮЛ">
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="СвФЛ"/>
            <xsl:if test="СвНомТел">
                <xsl:apply-templates select="СвНомТел"/>
            </xsl:if>
            <xsl:if test="СвРождФЛ">
                <xsl:apply-templates select="СвРождФЛ"/>
            </xsl:if>
            <xsl:if test="УдЛичнФЛ">
                <xsl:apply-templates select="УдЛичнФЛ"/>
            </xsl:if>
            <xsl:if test="АдресМЖРФ">
                <xsl:apply-templates select="АдресМЖРФ"/>
            </xsl:if>
            <xsl:if test="АдрМЖИн">
                <xsl:apply-templates select="АдрМЖИн"/>
            </xsl:if>
        </xsl:template>
        <xsl:template name="СвРождФЛ">
         
        </xsl:template>
        <xsl:template name="УдЛичнФЛ">          
        </xsl:template>
        <xsl:template name="АдресМЖРФ">
        
        </xsl:template>
        <xsl:template name="АдрМЖИн">
            
        </xsl:template>
        <xsl:template name="УдЛичнФл">
            
        </xsl:template>
        <xsl:template name="СвДовУпрЮЛ">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о доверительном управляющем - ЮЛ </td>
            </tr>
            <xsl:apply-templates select="НаимИННДовУпр"/>
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>         
        </xsl:template>
        <xsl:template name="СвДовУпрФЛ">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о доверительном управляющем - ФЛ </td>
            </tr>
            <xsl:apply-templates select="СвФЛ"/>
            <xsl:apply-templates select="СвРождФЛ"/>
            <xsl:apply-templates select="УдЛичнФЛ"/>
            <xsl:apply-templates select="АдресМЖРФ"/>
            <xsl:apply-templates select="АдрМЖИн"/>
            
            <xsl:if test="ГРНДатаПерв">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                    <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                </tr>
            </xsl:if>
        </xsl:template>    
        <xsl:template name="ЛицоУпрНасл">
            <tr>
                <td colspan="3" style="text-align:center">Сведения о лице, осуществляющем управление долей, переходящей в порядке наследования  </td>
            </tr>
            <tr>
                 <td class="num" align="center"></td>
                 <td>Дата открытия наследства (дата смерти участника)</td>
                 <td><xsl:value-of select="@ДатаОткрНасл"/></td>                
             </tr>
             <xsl:apply-templates select="СвФЛ"/>
             <xsl:apply-templates select="СвРождФЛ"/>
             <xsl:apply-templates select="УдЛичнФЛ"/>
             <xsl:apply-templates select="АдресМЖРФ"/>
             <xsl:apply-templates select="АдрМЖИн"/>
             <xsl:if test="ГРНДатаПерв">
                 <tr>
                     <td class="num" align="center"></td>
                     <td>ГРН и дата внесения в ЕГРЮЛ сведений о данном лице</td>
                     <td><xsl:value-of select="ГРНДатаПерв/@ГРН"/><br/><xsl:value-of select="ГРНДатаПерв/@ДатаЗаписи"/></td>
                 </tr>
             </xsl:if>
        </xsl:template>
        <xsl:template name="НаимИННДовУпр">
            <xsl:if test="@ОГРН">
               <tr>
                    <td class="num" align="center"></td>
                    <td>Основной государственный регистрационный номер юридического лица</td>
                    <td><xsl:value-of select="@ОГРН"/></td>                
                </tr> 
            </xsl:if>
            <xsl:if test="@ИНН">
                <tr>
                    <td class="num" align="center"></td>
                    <td>ИНН юридического лица</td>
                    <td><xsl:value-of select="@ИНН"/></td>                
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>Полное наименование юридического лица</td>
                <td><xsl:value-of select="@НаимЮЛПолн"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="СвНедДанДолжнФЛ">
            <tr>
                <td colspan="3" style="text-align:center"></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>style="text-align:left">Признак недостоверности данных</td>
                <td><xsl:value-of select="@ПризнНедДанДолжнФЛ"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Текст о недостоверности сведений, выводимый в выписке в строке с наименованием "Дополнительные сведения"</td>
                <td><xsl:value-of select="@ТекстНедДанДолжнФЛ"/></td>                
            </tr>
            <xsl:if test="РешСудНедДанДолжнФЛ">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения о решении суда, на основании которого указанные сведения признаны недостоверными</td>
                    <td><xsl:value-of select="РешСудНедДанДолжнФЛ/@КНаимСуда"/> <br/>
                        Решение №<xsl:value-of select="РешСудНедДанДолжнФЛ/@Номер"/> от <xsl:value-of select="РешСудНедДанДолжнФЛ/@Дата"/>
                    </td>              
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
            
        </xsl:template>
        <xsl:template name="СвДискв"> 
            <tr>
                <td class="num" align="center"></td>
                <td>Дата начала дисквалификации</td>
                <td><xsl:value-of select="@ДатаНачДискв"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Дата окончания дисквалификации</td>
                <td><xsl:value-of select="@ДатаОкончДискв"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Дата вынесения судебным органом постановления о дисквалификации </td>
                <td><xsl:value-of select="@ДатаРеш"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="СвНедДанУчр">
            <tr>
                <td colspan="3" style="text-align:center"></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>style="text-align:left">Признак недостоверности данных</td>
                <td><xsl:value-of select="@ПризнНедДанУчр"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>Текст о недостоверности сведений, выводимый в выписке в строке с наименованием "Дополнительные сведения"</td>
                <td><xsl:value-of select="@ТекстНедДанУчр"/></td>                
            </tr>
            <xsl:if test="РешСудНедДанУчр">
                <tr>
                    <td class="num" align="center"></td>
                    <td>Сведения о решении суда, на основании которого указанные сведения признаны недостоверными</td>
                    <td><xsl:value-of select="РешСудНедДанУчр/@КНаимСуда"/> <br/>
                        Решение №<xsl:value-of select="РешСудНедДанУчр/@Номер"/> от <xsl:value-of select="РешСудНедДанУчр/@Дата"/>
                    </td>              
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>ГРН и дата внесения в ЕГРЮЛ записи, содержащей указанные сведения</td>
                <td><xsl:value-of select="ГРНДата/@ГРН"/><br/><xsl:value-of select="ГРНДата/@ДатаЗаписи"/></td>
            </tr> 
        </xsl:template>
</xsl:stylesheet>