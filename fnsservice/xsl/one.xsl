<?xml version="1.0" encoding="windows-1251"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="1.0">
    <xsl:output method="html"></xsl:output>
    <xsl:template match="/">
        <xsl:apply-templates/>
    </xsl:template>
    <xsl:template match="/����"> 
           <div>                   
                   <table class="table table-sm" border="0" cellpadding="1" align="center" width="100%">
                       <tr id= "General">                           
                           <td align="center">�������</td>                             
                       </tr>
                       <tr>
                          <td align="center">�� ������� ���������������� ������� ����������� ���</td>                                               
                       </tr>
                       <tr> </tr>
                       <tr>
                           <td align="center">
                              <xsl:value-of select="��������/@����������"/>                           
                          </td>                                            
                       </tr>
                       <tr>
                           <td align="rigth">
                            ���� <xsl:value-of select="@����"/>
                          </td>                                               
                       </tr>
                       <tr>
                           <td align="rigth">
                               ���/��� <xsl:value-of select="@���"/>/<xsl:value-of select="@���"/>
                           </td>                                               
                       </tr>
                       <tr>
                           <td align="rigth">
                               �� ��������� �� <xsl:value-of select="@�������"/>
                           </td>
                       </tr>
                    </table> 
                   <table class="table table-sm table-bordered" border="1" cellpadding="3" align="center" width="100%">
                    <tr>
                        <th width="7%">N �/�</th>
                        <th>������������ ����������</th>
                        <th>�������� ����������</th>
                    </tr>
                       <tr>
                           <td align="center">1</td>
                           <td align="center">2</td>
                           <td align="center">3</td>
                       </tr>  
                       <xsl:apply-templates select="��������"/>                                  
                       <xsl:apply-templates select="���������"/>
                       <xsl:apply-templates select="������������"/>
                       <xsl:apply-templates select="�������"/>
                       <xsl:apply-templates select="��������"/>
                       <xsl:for-each select="��������">
                           <xsl:call-template name="��������"/>
                       </xsl:for-each>                       
                       <xsl:apply-templates select="���������"/>
                       <xsl:apply-templates select="��������"/>
                       <xsl:apply-templates select="�������"/>
                       <xsl:apply-templates select="��������"/> 
                       <xsl:apply-templates select="��������"/>
                       <xsl:apply-templates select="�����������"/>
                       <xsl:if test="��������">
                           <tr>
                               <td id ="SvUpOrg" colspan="3" style="text-align:center"><b>�������� �� ����������� �����������</b></td>
                           </tr>
                           <xsl:for-each select="��������">
                               <xsl:call-template name="��������"/>                            
                           </xsl:for-each>
                       </xsl:if>                 
                       <xsl:if test="�����������">
                           <tr>
                                <td id="SvDoljFL" colspan="3" style="text-align:center"><b>�������� � �����, ������� ����� ��� ������������ ����������� �� ����� ������������ ����  </b> </td>
                            </tr>
                            <xsl:for-each select="�����������">
                                <xsl:call-template name="�����������"/>                            
                           </xsl:for-each>
                       </xsl:if>
                       <xsl:if test="���������">
                           <tr>
                               <td id="SvUchr" colspan="3" style="text-align:center"><b>�������� �� ����������� (����������) ������������ ���� </b> </td>
                           </tr>
                           <xsl:for-each select="���������">
                               <xsl:call-template name="���������"/> 
                           </xsl:for-each>
                           
                       </xsl:if>
                       <xsl:apply-templates select="���������"/>
                       <xsl:apply-templates select="��������������"/>
                       <xsl:if test="�������">
                            <tr>
                                <td id="SvOKWED" colspan="3" style="text-align:center"><b>�������� � ����� ������������� ������������ �� ��������������� �������������� ����� ������������� ������������ </b> </td>
                            </tr>                       
                            <xsl:for-each select="�������">
                                <xsl:call-template name="�������"/>                               
                            </xsl:for-each>
                       </xsl:if>
                       <xsl:if test="����������">
                           <tr>
                           <td id="SvLicense" colspan="3" style="text-align:center"><b>�������� � ���������, �������� �� </b> </td>
                           </tr>
                            <xsl:for-each select="����������">
                                <xsl:call-template name="����������"/>                             
                            </xsl:for-each>
                       </xsl:if>
                       <xsl:apply-templates select="���������"/>                       
                       <xsl:if test="�������">
                           <tr>
                               <td id="SvReorg" colspan="3" style="text-align:center"><b>�������� �� ������� � ������������� </b> </td>
                           </tr>
                           <xsl:for-each select="�������">
                                <xsl:call-template name="�������"/>   
                           </xsl:for-each>
                       </xsl:if>
                       <xsl:if test="�������">
                           <tr>
                               <td id="SvPredSh" colspan="3" style="text-align:center"><b>�������� � �������������������� </b> </td>
                           </tr>
                       <xsl:for-each select="�������">
                           <xsl:call-template name="�������"/>   
                       </xsl:for-each>
                       </xsl:if>
                       <xsl:if test="����������">
                           <tr>
                               <td id="SvKFHPredSh" colspan="3" style="text-align:center"><b>�������� � ������������ (����������) ���������, �� ���� ��������� �������� ������� ����������� ���� </b> </td>
                           </tr>
                       <xsl:for-each select="����������">
                           <xsl:call-template name="����������"/>   
                       </xsl:for-each>
                       </xsl:if>
                       <xsl:if test="�������">
                           <tr>
                               <td id="SvPreem" colspan="3" style="text-align:center"><b>�������� � ������������ (����������) ���������, �� ���� ��������� �������� ������� ����������� ���� </b> </td>
                           </tr>
                        <xsl:for-each select="�������">
                            <xsl:call-template name="�������"/>   
                        </xsl:for-each>
                             
                       </xsl:if>
                       <xsl:apply-templates select="����������"/>
                       <tr>
                           <td id="EGRULrecords" colspan="3" style="text-align:center"><b>�������� � �������, ��������� � ������ ��������������� ������ ����������� ��� </b> </td>
                       </tr>
                       <xsl:for-each select="����������">
                           <xsl:call-template name="����������"/>   
                       </xsl:for-each>              
                   </table> 
                   <div id="bottom" class="anchor"></div>
               </div>
              
            </xsl:template>
        <xsl:template match="��������">
            
            <tr>
                <td id= "Name" colspan="3" style="text-align:center"><b>������������ </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">������ ������������</td>
                <td align="left"><xsl:value-of select="@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">����������� ������������</td>
                <td align="left"><xsl:value-of select="@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td align="left"><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>
        </xsl:template>
        <xsl:template match="���������">
            <tr>
                <td id = "Address" colspan="3" style="text-align:center"><b>����� (����� ����������) </b> </td>
                <xsl:apply-templates select="�������">
                </xsl:apply-templates>
            </tr>          
            <xsl:for-each select="������������">
                <xsl:call-template name="������������"/>                             
            </xsl:for-each>                 
        </xsl:template>
        <xsl:template name="������������">
            <tr>                      
                <td class="num" align="center"></td>
                <td align="left">�������������� �������� </td>
                <td align="left"><xsl:value-of select="@���������������"/></td>
            </tr>
            <xsl:if test="������������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� � ������� ����, �� ��������� �������� ����� ������� �������������</td>
                    <td><xsl:value-of select="������������/@���������"/> <br/>
                        ������� �<xsl:value-of select="������������/@�����"/> �� <xsl:value-of select="������������/@����"/>
                    </td>              
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="�������"> 
            <tr>
                <td class="num" align="center"></td>
                <td align="left">�������� ������</td>
                <td align="left"><xsl:value-of select="@������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">������� ���������� ���������</td>
                <td align="left"><xsl:value-of select="@���������"/> - <xsl:value-of select="������/@���������"/>&#160;<xsl:value-of select="������/@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">��� ������ �� �����</td>
                <td align="left"><xsl:value-of select="@�����������"/></td>
            </tr> 
            <xsl:if test="�����">
            <tr>
                <td class="num" align="center"></td>
                <td align="left">����� (������� � �.�.)</td>
                <td align="left"><xsl:value-of select="�����/@��������"/>&#160;<xsl:value-of select="�����/@���������"/></td>
            </tr>
            </xsl:if>    
            <xsl:if test="����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td align="left">���������� ����� (���� � �.�.)</td>
                    <td align="left"><xsl:value-of select="����������/@�������������"/>&#160;<xsl:value-of select="����������/@��������������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="�����">
                <tr>
                    <td class="num" align="center"></td>
                    <td>����� (���� � �.�.)</td>
                    <td><xsl:value-of select="�����/@��������"/>&#160;<xsl:value-of select="�����/@���������"/></td>
                </tr>
                
            </xsl:if>
            <xsl:if test="�����">
                <tr>
                    <td class="num" align="center"></td>
                    <td>����� (��������, �������� � �.�.)</td>
                    <td><xsl:value-of select="�����/@��������"/>&#160;<xsl:value-of select="�����/@���������"/></td>
                </tr>
                
            </xsl:if>
            <xsl:if test="@���">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� (�������� � �.�.)</td>
                    <td><xsl:value-of select="@���"/></td>
                </tr>                
            </xsl:if>
            <xsl:if test="@������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>������ (�������� � �.�.)</td>
                    <td><xsl:value-of select="@������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="@�����">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� (���� � �.�.)</td>
                    <td><xsl:value-of select="@�����"/></td>
                </tr>   
            </xsl:if>                   
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="�������">
            <tr>
                <td id="ObrUL" colspan="3" style="text-align:center"><b>�������� � ����������� (�����������) ������������ ���� </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ����������� ������������ ����</td>
                <td><xsl:value-of select="�������/@����������"/> - <xsl:value-of select="�������/@�����������"/> </td>
            </tr>            
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� ��������������� ��������������� ����� ������������ ����</td>
                    <td><xsl:value-of select="@����"/></td>
                </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���� ���������� ����</td>
                <td><xsl:value-of select="@��������"/></td>
            </tr>
            <xsl:if test="@������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��������������� �����, ����������� ����������� ������������ ���� �� 1 ���� 2002 ����, ��� ��������������� ����� ������������ ���� �� ���������� ���������� ���� ��� ���������� ������ ������������ �������� ����������� �� ���� �������� � �� � ����������� � ������� �� ����� ��������� - ���������� ���� � ������ ������������ �������� �����������</td>
                    <td><xsl:value-of select="@������"/></td>
                </tr> 
            </xsl:if>
            <xsl:if test="@�������">
               <tr>
                   <td class="num" align="center"></td>
                   <td>���� ����������� ������������ ���� �� 1 ���� 2002 ����, � ����� � ��������� �� ������������������ �� ���������� ���������� ���� ��� ���������� ������ ������������ �������� ����������� �� ���� �������� � �� � ����������� � ������� �� ����� ��������� - ���������� ���� � ������ ������������ �������� �����������</td>
                   <td><xsl:value-of select="@�������"/></td>
               </tr>
            </xsl:if>
            <xsl:if test="@������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>������������ ������, ������������������� ����������� ���� �� 1 ���� 2002 ����, � ����� � ��������� �� ������������������ �� ���������� ���������� ���� ��� ���������� ������ ������������ �������� ����������� �� ���� �������� � �� � ����������� � ������� �� ����� ��������� - ���������� ���� � ������ ������������ �������� ����������� </td>
                    <td><xsl:value-of select="@������"/></td>
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/> <p><xsl:value-of select="�������/@����������"/></p></td>
            </tr>
        </xsl:template>
        <xsl:template match="�������">   
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� ������� ����������� �� ����������� �����</td>
                    <td><xsl:value-of select="@����������"/></td>
                </tr>
                <tr>
                    <td class="num" align="center"></td>
                    <td>������������ ������� ����������� ������������ ����</td>
                    <td><xsl:value-of select="@�����������"/></td>
                </tr>
            </xsl:template>
        <xsl:template match="��������">            
            <tr>
                <td class="num" align="center"></td>
                <td>��� ������ �� ����������� ����</td>
                <td><xsl:value-of select="@�����"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td id="SvRegOrg">������������ ��������������� (����������) ������</td>
                <td><xsl:value-of select="@������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>����� ��������������� ������</td>
                <td><xsl:value-of select="@�����"/></td>
            </tr> 
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/> <br/> <xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template name="��������">
            <tr>
                <td id="SvStatus" colspan="3" style="text-align:center"><b>�������� � ��������� (�������) ������������ ����</b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� � ���������������� (�������) ������������ ����</td>
                <td><xsl:value-of select="��������/@�����������"/> - <xsl:value-of select="��������/@������������"/></td>
            </tr>
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� � ������� � ����������� ���������� �������������� �� �� ����� � ��� ���������� </td>
                    <td>������� � <xsl:value-of select="�����������/@��������"/> �� - <xsl:value-of select="�����������/@�������"/>
                        <br/>����������� <xsl:value-of select="�����������/@��������������"/> � � <xsl:value-of select="�����������/@������������"/> 
                    </td>
                </tr>
            </xsl:if>            
        </xsl:template>
        <xsl:template match="���������">
            <tr>
                <td id="SvPrekUl" colspan="3" style="text-align:center"><b>�������� � ����������� ������������ ����</b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ����������� ������������ ����</td>
                <td><xsl:value-of select="���������/@������������"/>  - <xsl:value-of select="���������/@�������������"/>
                    <xsl:if test="�����������">
                        <br/> ����������� <xsl:value-of select="�����������/@��������������"/> � � <xsl:value-of select="�����������/@������������"/> 
                    </xsl:if>                    
                </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���� ����������� ������������ ����</td>
                <td><xsl:value-of select="@�����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� � �������������� (���������) ������, ������� ������ � ����������� ������������ ����</td>
                <td><xsl:value-of select="��������/@�����"/> - <xsl:value-of select="��������/@������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/> <xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="������������">
            <tr>
                <td id = "Email" colspan="3" style="text-align:center"><b>�������� �� ������ ����������� ����� ������������ ����</b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td><p style="text-align:left">����� ����������� �����</p></td>
                <td><p style="text-align:left"><xsl:value-of select="@E-mail"/></p></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td><p style="text-align:left">��� � ���� �������� � ����� ������, ���������� ��������� ��������</p></td>
                <td><p style="text-align:left"><xsl:value-of select="�������/@���"/></p> <p><xsl:value-of select="�������/@����������"/></p></td>
            </tr> 
        </xsl:template>
        <xsl:template match="��������">
            <tr>
                <td id ="SvUchN" colspan="3" style="text-align:center"><b>�������� �� ����� � ��������� ������</b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���</td>
                <td><xsl:value-of select="@���"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���</td>
                <td><xsl:value-of select="@���"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���� ���������� �� ���� � ��������� ������</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� � ��������� ������, � ������� ����������� ���� ������� (��� ��, ������������ ������������ - ��������) �� �����</td>
                <td><xsl:value-of select="����/@�����"/> - <xsl:value-of select="����/@������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/> <xsl:value-of select="�������/@����������"/></td>
            </tr>           
        </xsl:template>
        <xsl:template match="�������">
            <tr>
                <td id="SvRegPF" colspan="3" style="text-align:center"><b>�������� � ����������� ������������ ���� � �������� ������������ � ��������������� ������ ����������� ����� ���������� ��������� </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��������������� ����� � ��������������� ������ ����������� ����� ���������� ���������</td>
                <td><p style="text-align:left"><xsl:value-of select="@��������"/></p></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���� ����������� ������������ ���� � �������� ������������</td>
                <td><xsl:value-of select="@�������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� � ��������������� ������ ����������� ����� ���������� </td>
                <td><xsl:value-of select="�������/@�����"/> - <xsl:value-of select="�������/@������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="��������">
            <tr>
                <td id="SvRegFSS" colspan="3" style="text-align:center"><b>�������� � ����������� ������������ ���� � �������� ������������ � �������������� ������ ����� ����������� ����������� ���������� ��������� </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��������������� ����� � �������������� ������ ����� ����������� ����������� ���������� ���������</td>
                <td><xsl:value-of select="@���������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���� ����������� ������������ ���� � �������� ������������</td>
                <td><xsl:value-of select="@�������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� �� �������������� ������ ����� ����������� ����������� ���������� ���������</td>
                <td><xsl:value-of select="��������/@������"/> - <xsl:value-of select="��������/@�������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="��������">
            <tr>
                <td id="SvUstKap" colspan="3" style="text-align:center"><b>�������� � ������� ���������� � ������������� ���������� ������������ ����������� ��������� �������� (����������� ��������, ��������� �����, ������� �����) </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������������ ���� ��������</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������ � ������</td>
                <td><xsl:value-of select="@������"/></td>
            </tr>
            <xsl:if test="���������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>���� ����� � ��������</td>
                    <td><xsl:value-of select="���������/@������"/>/<xsl:value-of select="���������/@��������"/></td>
                </tr>
                
            </xsl:if>
            <xsl:if test="��������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� � ���������� �������������� �������� � �������� ���������� ��������� ��������</td>
                    <td>���������� �� <xsl:value-of select="��������/@��������"/> �� ������� �� /<xsl:value-of select="��������/@�������"/></td>
                </tr>
            </xsl:if>            
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="�����������">
            <tr>
                <td id="SvTipUS" colspan="3" style="text-align:center"><b>�������� �� ������������� ����������� ����� �������� ������ </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� � ����������� �������� ���� �� ����������� �������� ������</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="����������">
            <tr>
                <td colspan="3" style="text-align:center">���� � �������� �������� (���������� ��������, �������� �����, ������ �����), ��������� � ����� </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>����������� ��������� ���� � ������</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
            
            <xsl:apply-templates select="����������"/>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="����������">
            <tr>
                <td class="num" align="center"></td>
                <td>������ ���� (� ��������� ��� � ���� ����� - ���������� ��� �������) </td>
                <td>
                    <xsl:if test="�������">
                        <xsl:value-of select="�������"/>
                    </xsl:if>
                    <xsl:if test="@���������">
                        <xsl:value-of select="���������"/>
                    </xsl:if>
                    <xsl:if test="@���������">
                        <xsl:value-of select="���������/@������"/> / <xsl:value-of select="����������/���������/@��������"/>
                    </xsl:if>
                </td> 
            </tr>
        </xsl:template>
        <xsl:template name="��������">            
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                    <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                </tr>
            </xsl:if>            
            <tr>
                <td colspan="3" style="text-align:center">�������� � ������������ � (��� �������) ���� � ��� �� - ����������� �����������</td>
            </tr>
            <xsl:apply-templates select="���������"/>
            <xsl:if test="�������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � ����������� ������������ �� � ������ �������������, ��������� � ����� </td>
                </tr>
                <xsl:apply-templates select="�������"/>
            </xsl:if>
            <xsl:if test="��������������">
                <tr>
                    <td colspan="3" style="text-align:center"></td>
                </tr>
                <xsl:for-each select="��������������">
                    <xsl:call-template name="��������������"/>                             
                </xsl:for-each>
            </xsl:if>
            <xsl:if test="�������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � ������������ ����������������� ��� ������� � ���������� ���������, ����� ������� ����������� �� ������������ ���������� ����������� �����������</td>
                </tr> 
                    <xsl:apply-templates select="��������"/>
            </xsl:if>
            <xsl:if test="�������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� �� ������ ����������� ����������� � ���������� ���������</td>
                </tr> 
                <xsl:apply-templates select="�������"/>
            </xsl:if>
            <xsl:if test="��������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � ���������� ��������</td>
                <xsl:apply-templates select="��������"/>
                </tr>
            </xsl:if>
            <xsl:if test="��������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � ����, ����� ������� ����������� ����������� ���� ������������ ���������� ����������� �����������</td>
                    <xsl:apply-templates select="��������"/>
                </tr>
            </xsl:if>
            
        </xsl:template>
        <xsl:template match="���������">
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
            <tr>
                <td class="num" align="center"></td>
                <td>�������� ��������������� ��������������� ����� ������������ ����</td>
                <td><p style="text-align:left"><xsl:value-of select="@����"/></p></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� ������������ ����</td>
                <td><xsl:value-of select="@���"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������ ������������ ����</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
            
            
        </xsl:template>
        <xsl:template match="�������">
            <tr>
                <td class="num" align="center"></td>
                <td>��� ������ �������������</td>
                <td><xsl:value-of select="@����"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������������ ������ �������������</td>
                <td><xsl:value-of select="@���������"/></td>
            </tr>
            <xsl:if test="@�������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>���� �����������</td>
                    <td><xsl:value-of select="@�������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="@��������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��������������� �����</td>
                    <td><xsl:value-of select="@��������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="@����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>������������ ��������������� ������</td>
                    <td><xsl:value-of select="@����������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="@������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>����� (����� ����������) � ������ �������������</td>
                    <td><xsl:value-of select="@������"/></td>
                </tr>   
            </xsl:if>
                     
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="�����������">
            <tr>
                <td colspan="3" style="text-align:center"></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
            </tr>             
            <xsl:apply-templates select="����"/>
            <xsl:apply-templates select="�������"/>    
            <xsl:if test="��������">
                 <xsl:apply-templates select="��������"/>
            </xsl:if>           
            <xsl:if test="���������������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � ��������������� ������ � ����, ������� ����� ��� ������������ ����������� �� ����� ������������ ���� </td>
                </tr>
                <xsl:apply-templates select="���������������"/> 
            </xsl:if>
            <!---�� -->
            <xsl:if test="��������">
                <xsl:apply-templates select="��������"/>
            </xsl:if>
            <xsl:if test="��������">
                <xsl:apply-templates select="��������"/>
            </xsl:if>
            <xsl:if test="���������">
                <xsl:apply-templates select="���������"/>
            </xsl:if>
            <xsl:if test="�������">
                <xsl:apply-templates select="�������"/>
            </xsl:if>
            <xsl:if test="�������">
                <tr>
                    <td colspan="3" style="text-align:center"></td>
                </tr>
                <xsl:for-each select="�������">
                    <xsl:call-template name="�������"/>                             
                </xsl:for-each>
            </xsl:if>
            
        </xsl:template>
        <xsl:template match="�������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � ��������� �� </td>
            </tr>
            <xsl:if test="������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>������</td>
                    <td><xsl:value-of select="@������"/></td>
                </tr>
            </xsl:if>
            
            <tr>
                <td class="num" align="center"></td>
                <td>��� ������������ ���� �� ����������� ������ </td>
                <td><xsl:value-of select="@��������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������������ ���� ������������ ���� �� ����������� ������ </td>
                <td><xsl:value-of select="@������������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������������ ���������</td>
                <td><xsl:value-of select="@���������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td align="left"><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>
        </xsl:template>
        <xsl:template match="����">
            <tr>
                <td class="num" align="center"></td>
                <td>�������</td>
                <td><xsl:value-of select="@�������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���</td>
                <td><xsl:value-of select="@���"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��������</td>
                <td><xsl:value-of select="@��������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���</td>
                <td><xsl:value-of select="@�����"/></td>
            </tr>  
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="��������">
            <tr>
                <td class="num" align="center"></td>
                <td>���������� �������</td>
                <td><xsl:value-of select="@������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"><p style="text-align:center"></p></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template name="���������">
            <xsl:for-each select="��������">
                <xsl:call-template name="��������"/>                
            </xsl:for-each>
            <xsl:for-each select="�������">
                <xsl:call-template name="�������"/>                
            </xsl:for-each>
            <xsl:for-each select="�����">
                <xsl:call-template name="�����"/>                
            </xsl:for-each>
            <xsl:for-each select="����������">
                <xsl:call-template name="����������"/>
            </xsl:for-each>
            <xsl:for-each select="������">                               
                <xsl:call-template name="������"/>
            </xsl:for-each>
            
        </xsl:template>
        <xsl:template name="�������">
            <tr>
                <td colspan="3" style="text-align:center">�������� �� ���������� (���������) - ����������� ����������� ���� </td>
            </tr>
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                        <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                        <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="���������"/>
            <xsl:if test="�������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � ����������� � ������ ������������� </td>
                </tr>
                <xsl:apply-templates select="�������"/>
            </xsl:if>
            <xsl:for-each select="�����������">
                <xsl:call-template name="�����������">                               
                </xsl:call-template>
            </xsl:for-each>
            <xsl:if test="����������">
                <xsl:apply-templates select="����������"/> 
            </xsl:if>
            <xsl:for-each select="�������">
                <xsl:call-template name="�������"/>                
            </xsl:for-each>           
        </xsl:template>
        <xsl:template name="�����">
            <tr>
                <td colspan="3" style="text-align:center">�������� �� ���������� (���������) - ���������� ���� </td>
            </tr>
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                    <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                </tr>
            </xsl:if>            
            <xsl:apply-templates select="����"/>
            <xsl:for-each select="�����������">
                <xsl:call-template name="�����������"/>                
            </xsl:for-each>
            <xsl:if test="��������"> 
                <tr>
                    <td colspan="3" style="text-align:center">�������� � �������� �� </td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="��������"/>            
            <xsl:apply-templates select="��������"/>
            <xsl:apply-templates select="���������"/>
            <xsl:apply-templates select="�������"/>
            <xsl:apply-templates select="����������"/>           
            <xsl:for-each select="�������">
                <xsl:call-template name="�������">                               
                </xsl:call-template>
            </xsl:for-each>
            <xsl:apply-templates select="����������"/> 
            <xsl:apply-templates select="����������"/> 
            <xsl:apply-templates select="�����������"/>
        </xsl:template>
        <xsl:template name="����������">
            <tr>
                <td colspan="3" style="text-align:center">�������� �� ���������� (���������) - ���������� ���������, �������� ���������� ���������, ������������� �����������</td>
            </tr>
            <xsl:apply-templates select="����������"/>
            <xsl:for-each select="�����������">
                <xsl:call-template name="�����������">                               
                </xsl:call-template>
            </xsl:for-each>
            <xsl:apply-templates select="����������"/>           
            <xsl:for-each select="�����������">
                <xsl:call-template name="�����������"/>
            </xsl:for-each>
            <xsl:for-each select="����������">
                <xsl:call-template name="����������"/>
            </xsl:for-each>
            <xsl:for-each select="�������">
                <xsl:call-template name="�������"/>
            </xsl:for-each>            
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                    <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                </tr>
            </xsl:if>            
        </xsl:template>
        <xsl:template name="��������">
            <tr>
                <td colspan="3" style="text-align:center">�������� �� ���������� (���������) - ���������� ����������� ���� </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
            </tr>
            <xsl:apply-templates select="���������"/>
            <xsl:if test="�����������">
                <xsl:apply-templates select="�����������"/>
            </xsl:if>
            <xsl:for-each select="�����������">
                <xsl:call-template name="�����������"/>
            </xsl:for-each>
                <xsl:apply-templates select="����������"/>
            <xsl:for-each select="�������">
                <xsl:call-template name="�������"/>
            </xsl:for-each>
        </xsl:template>
        <xsl:template name="�������">
            <tr>
                <td colspan="3" style="text-align:center">�������� �� ����������� ���� ���������, ��������� � ����� </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� �����������</td>
                <td><xsl:value-of select="@��������"/></td>
            </tr>
            <xsl:if test="@���������������">
                <tr>
                <td class="num" align="center"></td>
                <td>���� ����������� ��� ������� ����������� �����</td>
                <td><xsl:value-of select="@���������������"/></td>
            </tr>
                </xsl:if>
            <xsl:if test="������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� � ������� ��������� ������, �� �������� �� ���� ���������� (���������) �������� �����������</td>
                    <td><xsl:value-of select="������/@���������"/> <br/>
                        ������� �<xsl:value-of select="������/@�����"/> �� <xsl:value-of select="������/@����"/>
                    </td>              
                </tr>
            </xsl:if>
            <xsl:if test="�������������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � ��������������� - �� </td>
                </tr>
            </xsl:if> 
            <xsl:if test="�������������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � ��������������� - �� </td>
                </tr>
            </xsl:if>           
            <tr>
                <td class="num" align="center"></td>
                <td align="left">��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td align="left"><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>
            
        </xsl:template>
        <xsl:template name="�����������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � ����������� ���������� (���������) �� 01.07.2002 �</td>
            </tr>
            <xsl:if test="������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��������������� �����, ����������� ������������ ���� �� 1 ���� 2002 ����</td>
                    <td><xsl:value-of select="@������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="�������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>���� ����������� ������������ ���� �� 1 ���� 2002 ����</td>
                    <td><xsl:value-of select="@�������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>������������ ������, ������������������� ����������� ���� �� 1 ���� 2002 ����</td>
                    <td><xsl:value-of select="@������"/></td>
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template name="�����������">
            <xsl:apply-templates select="���������"/>            
        </xsl:template>
        <xsl:template name="����������">
        <xsl:apply-templates select="����"/>
        <xsl:apply-templates select="��������"/>
        <xsl:apply-templates select="��������"/>
        <xsl:apply-templates select="���������"/>
        <xsl:apply-templates select="�������"/>
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                    <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                </tr>
            </xsl:if>   
        </xsl:template>
        <xsl:template name="���������">
            <tr>
                <td class="num" align="center"></td>
                <td>�������� (�������������� �����������) ������� ��������������� �����</td>
                <td><xsl:value-of select="@�������"/></td>
            </tr>        
            <xsl:if test="�������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                    <td><xsl:value-of select="�������/@���"/> <br/> <xsl:value-of select="�������/@����������"/></td>
                </tr>  
            </xsl:if>        
        </xsl:template>
        <xsl:template name="������������">
            <tr>
                <td class="num" align="center"></td>
                <td>������������ � (��� �������) ���� � ��� ����������� �������� ������� ��������������� �����</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>        
            <xsl:if test="�������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                    <td><xsl:value-of select="�����������/@���"/> <br/> <xsl:value-of select="�����������/@����������"/></td>
                </tr>  
            </xsl:if>
        </xsl:template>
        <xsl:template name="����������">
            <tr>
               <td class="num" align="center"></td>
               <td>��� ���� ����������</td>
                <td><xsl:value-of select="@�������������"/></td>
             </tr>
             <xsl:if test="@������">
                 <tr>
                     <td class="num" align="center"></td>
                     <td>������������ �������������� �����������</td>
                     <td><xsl:value-of select="@������"/></td>
                 </tr>
                </xsl:if>
                <xsl:if test="@������">
                    <tr>
                        <td class="num" align="center"></td>
                        <td>��� �������� ���������� ���������, ������� �������� ����������� (����������) ������������ ���� ��� �� ���������� �������� ��������� ������������� �����������, ������� �������� ����������� (����������) ������������ ����</td>
                        <td><xsl:value-of select="@���������"/></td>
                    </tr>
                </xsl:if>
                <xsl:if test="@������">
                    <tr>
                        <td class="num" align="center"></td>
                        <td>������������ �������� ���������� ���������</td>
                        <td><xsl:value-of select="@����������"/></td>
                    </tr>
                </xsl:if>
            </xsl:template>
        <xsl:template name="������">
             <tr>
                 <td colspan="3" style="text-align:center">�������� � ������ �������������� �����, � ������ ��������� �������� �������� ���� � �������� ��������  </td>
             </tr>
             <xsl:apply-templates select="���������"/>
             <xsl:for-each select="�����������">
                <xsl:call-template name="�����������"/>
             </xsl:for-each>    
                
             <xsl:if test="�����������">
               <tr>
                   <td><p style="text-align:center"></p></td>
                   <td><p style="text-align:left">��� � ���� �������� � ����� �������� � ������ ����</p></td>
                   <td><p style="text-align:left"><xsl:value-of select="�����������/@���"/></p> <p><xsl:value-of select="�����������/@����������"/></p></td>
               </tr>
             </xsl:if>
             <xsl:apply-templates select="������������"/>
             <xsl:apply-templates select="����������"/>
             <xsl:for-each select="�������">
                 <xsl:call-template name="�������"/>
             </xsl:for-each>
        </xsl:template>
        <xsl:template match="���������">
            <tr>
                <td id="SvDolOOO" colspan="3" style="text-align:center"><b>�������� � ���� � �������� �������� �������� � ������������ ����������������, ������������� ��������  </b> </td>
            </tr>
            <xsl:apply-templates select="����������"/>
            <xsl:if test="@����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>����������� ��������� ���� � ������</td>
                    <td><xsl:value-of select="@����������"/></td>
                </tr>
            </xsl:if>            
            <xsl:apply-templates select="����������"/>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="��������������">
            <tr>
                <td id="SvDerjReestrAO" colspan="3" style="text-align:center"><b>�������� � ��������� ������� ���������� ������������ �������� </b> </td>
            </tr>
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                    <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="������������"/>                
            
        </xsl:template>
        <xsl:template match="������������">
            <xsl:if test="@����">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� ��������������� ��������������� ����� ������������ ����</td>
                    <td><xsl:value-of select="@����"/></td>                
                </tr> 
            </xsl:if>
            <xsl:if test="@���">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� ������������ ����</td>
                    <td><xsl:value-of select="@���"/></td>                
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������ ������������ ����</td>
                <td><xsl:value-of select="@����������"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="����������">            
            <tr>
                <td class="num" align="center"></td>
                <td>����� � ����� ��������</td>
                <td><xsl:value-of select="@������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���� ��������</td>
                <td><xsl:value-of select="@�������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���� ������ �������� ��������</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
            <xsl:if test="@������������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>���� ��������� �������� ��������</td>
                    <td><xsl:value-of select="@������������"/></td>
                </tr>
            </xsl:if>            
            <tr>
                <td class="num" align="center"></td>
                <td>������������ �������������� ���� ������������, �� ������� ������ ��������</td>
                <td><xsl:value-of select="��������������"/>, </td>
                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� �� ������ ����� ������������� �������������� ���� ������������</td>
                <xsl:if test="��������������">
                    <td><xsl:value-of select="�������������"/>, </td>
                </xsl:if>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������������ �������������� ������, ��������� ��� ��������������� ��������</td>
                <td><xsl:value-of select="������������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� � ��������������� �������� ��������</td>
                    <td><xsl:value-of select="�����������/@�������������"/> <p><xsl:value-of select="�����������/@���������������"/></p></td>
            </tr>
            </xsl:if>
            
        </xsl:template>
        <xsl:template name="�������">
            <xsl:apply-templates select="��������"/>
            <tr>
                <td id="SvReorg" colspan="3" style="text-align:center"><b>�������� �� ������� � �������������</b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� �������� � ������ �������������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>
            <xsl:for-each select="���������������������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� ������, ������� � ����� ������� �������� �� ��������� ������� ����������� � ������������� ����������� ��� </td>
                    <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
                </tr>
            </xsl:for-each>
            <xsl:for-each select="���������">
                <xsl:call-template name="���������"/>
            </xsl:for-each>
        </xsl:template>
        <xsl:template name="���������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � ����������� �����, ����������� � �������������</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� ��������������� ��������������� ����� ������������ ����</td>
                <td><xsl:value-of select="@����"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������ ������������ ����</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� ������������ ����</td>
                <td><xsl:value-of select="@���"/></td>
            </tr>
            <xsl:if test="�����������">
               <tr>
                   <td class="num" align="center"></td>
                   <td>��������� ������������ ���� ����� ���������� �������������</td>
                   <td><xsl:value-of select="@�����������"/></td>
               </tr>
            </xsl:if>
        </xsl:template>
        <xsl:template name="�������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � �������������������� </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� ��������������� ��������������� ����� ������������ ����</td>
                <td><xsl:value-of select="@����"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� ������������ ����</td>
                <td><xsl:value-of select="@���"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������ ������������ ����</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
            <xsl:apply-templates select="��������������"/>            
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>
        </xsl:template>
        <xsl:template match="��������������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � ��, ����� ������������� �������� ��� ������ ������������������� ��� ������������� � ����� ��������� ��� ���������� � ������������� �������������� ��� ��������</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� ��������������� ��������������� ����� ������������ ����</td>
                <td><xsl:value-of select="@����"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������ ������������ ����</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� ������������ ����</td>
                <td><xsl:value-of select="@���"/></td>
            </tr>
            
        </xsl:template>
        <xsl:template name="����������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � ������������ (����������) ���������, �� ���� ��������� �������� ������� ����������� ���� </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������� (�����������) ���������</td>
                <td><xsl:value-of select="@������"/></td>
            </tr>
            <xsl:apply-templates select="����"/>
        </xsl:template>
        <xsl:template name="����������">
            <tr>
                <td id="SvKFHPreem" colspan="3" style="text-align:center"><b>�������� � ������������ (����������) ���������, ������� ������� � ����� � ����� � ����������� ��������� ������� ������������� (�����������) ��������� � ������������ � ������� ����� ������ ������������ ������� ���������� ��������� </b> </td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������� (�����������) ���������</td>
                <td><xsl:value-of select="@������"/></td>
            </tr>
            <xsl:apply-templates select="����"/>
        </xsl:template>
        <xsl:template name="�������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � �������������� </td>
            </tr>            
            <tr>
                <td class="num" align="center"></td>
                <td>�������� ��������������� ��������������� ����� ������������ ����</td>
                <td><xsl:value-of select="@����"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������ ������������ ����</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
            <xsl:if test="@���">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� ������������ ����</td>
                    <td><xsl:value-of select="@���"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="��������������"/>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template match="��������������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � ��, ������� ���� ������� � ����� ������� � �������� ��������������, ��� � �������� ������������� ������������� ��� ������������� � ����� ��������� ��� ���������� � ������������� �������������� ��� ��������</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� ��������������� ��������������� ����� ������������ ����</td>
                <td><xsl:value-of select="@����"/></td>
            </tr>            
            <xsl:if test="@���">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� ������������ ����</td>
                    <td><xsl:value-of select="@���"/></td>
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������ ������������ ����</td>
                <td><xsl:value-of select="@����������"/></td>
            </tr>
        </xsl:template>
        <xsl:template name="����������">
            <tr>
                <td colspan="3" style="text-align:center"><b><xsl:value-of select="position()"/></b> </td>
            </tr>           
            <tr>
                <td class="num" align="center"></td>
                <td>��������������� ��������������� ����� ������</td>
                <td><xsl:value-of select="@���"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���� �������� ������ � �����</td>
                <td><xsl:value-of select="@�������"/></td>
            </tr> 
            <tr>
                <td class="num" align="center"></td>
                <td>�������� � ������� �������� ������ � �����</td>
                <td><xsl:value-of select="������/@�������"/> - <xsl:value-of select="������/@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� � �������������� (���������) ������, ������� ������ � ����������� ������������ ����</td>
                <td><xsl:value-of select="��������/@�����"/> - <xsl:value-of select="��������/@������"/></td>
            </tr>
            <xsl:for-each select="��������">
                <xsl:call-template name="��������"/>   
            </xsl:for-each>
            <xsl:if test="�����������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � ����������, �������������� ��� �������� ������ � �����</td>
                </tr>
                <xsl:for-each select="�����������">                
                    <xsl:call-template name="�����������"/>   
                </xsl:for-each>    
            </xsl:if>           
            <xsl:for-each select="������">
                <xsl:call-template name="������"/>   
            </xsl:for-each>
            <xsl:if test="���������������/@���">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� ������, � ������� ������� �����������</td>
                    <td><xsl:value-of select="���������������/@���"/> �� <xsl:value-of select="���������������/@�������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="��������������/@���">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� ������, ������� �������� ����������������</td>
                    <td><xsl:value-of select="��������������/@���"/> �� <xsl:value-of select="��������������/@�������"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="�����������"/>
        </xsl:template>
        <xsl:template match="�����������">
            <xsl:if test="����������/@���">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� ������, ������� ������ �������� ����������������</td>
                    <td><xsl:value-of select="����������/@���"/> �� <xsl:value-of select="����������/@�������"/></td>
                </tr>                
            </xsl:if> 
            <xsl:for-each select="�����������">                
                <xsl:call-template name="�����������"/>
            </xsl:for-each>
        </xsl:template>
        <xsl:template name="�����������">
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� ������, ������� ������� ����������� � ����� � ����������� �������</td>
                <td><xsl:value-of select="@���"/> �� <xsl:value-of select="@�������"/></td>
            </tr>     
        </xsl:template>
        <xsl:template name="��������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � ��������� </td>
            </tr>
            <xsl:if test="�������/@���������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>���������</td>
                    <td><xsl:value-of select="�������/@��������"/> - <xsl:value-of select="�������/@���������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="����/@����">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� � ����������� ����, �� ����� �������� ��������� ���������</td>
                    <td><xsl:value-of select="����/@����"/>/<xsl:value-of select="����/@���"/> - <xsl:value-of select="����/@����������"/></td>
            </tr>
            </xsl:if>
            <xsl:if test="��������/@����">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� �� ����������� ��������</td>
                    <td><xsl:value-of select="��������/@����"/>/<xsl:value-of select="��������/@���"/> - <xsl:value-of select="��������/@����������"/></td>
            </tr>
            </xsl:if>
            <xsl:if test="����/��������/@�������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� � �� - ���������</td>
                    <td><xsl:value-of select="����/��������/@�������"/> <xsl:value-of select="����/��������/@���"/> <xsl:value-of select="����/��������/@��������"/>
                        <xsl:value-of select="����/��������/@�����"/></td>
                </tr>    
            </xsl:if>
                        
        </xsl:template>
        <xsl:template name="�����������">
            <tr>
                <td colspan="3" style="text-align:center"></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
               <td>������������ ���������</td>
               <td><xsl:value-of select="�������"/></td>
            </tr>
            <xsl:if test="������">
                    <tr>
                       <td class="num" align="center"></td>
                       <td>����� ���������</td>
                       <td><xsl:value-of select="������"/></td>
                   </tr> 
            </xsl:if>
            <xsl:if test="�������">
                    <tr>
                        <td class="num" align="center"></td>
                        <td>���� ���������</td>
                        <td><xsl:value-of select="�������"/></td>
                    </tr> 
            </xsl:if>            
        </xsl:template>
        <xsl:template name="������">
            <tr>
                <td class="num" align="center"></td>
                <td>�������� � �������������, �������������� ���� �������� ������ � ����� </td>
                <td><xsl:value-of select="@�����"/>&#160;<xsl:value-of select="@�����"/> �� <xsl:value-of select="@�����������"/></td>
            </tr> 
            <xsl:if test="��������������/@���">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                    <td><xsl:value-of select="��������������/@���"/><br/><xsl:value-of select="��������������/@����������"/></td>
                </tr> 
            </xsl:if>
            
        </xsl:template>
        <xsl:template name="�������">
            <tr>
                <td colspan="3" style="text-align:center"><b>�������� �� �������� ���� ������������ </b> </td>
            </tr>
            <xsl:if test="����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ������������ ���� ������������</td>
                    <td><xsl:value-of select="����������/@��������"/> - <xsl:value-of select="����������/@���������"/></td>
                </tr>
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                    <td><xsl:value-of select="����������/�������/@���"/><br/><xsl:value-of select="����������/�������/@����������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="����������">
                <tr>
                    <td colspan="3" style="text-align:center"><b>�������� � �������������� ���� ������������ </b> </td>
                </tr>
            <xsl:for-each select="����������">
                <xsl:call-template name="����������"/>   
            </xsl:for-each>
            </xsl:if>           
            
        </xsl:template>
        <xsl:template name="����������">
            <tr>
                <td colspan="3" style="text-align:center"><xsl:value-of select="position()"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ������������ ���� ������������</td>
                <td><xsl:value-of select="@��������"/> - <xsl:value-of select="@���������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>
        </xsl:template>
        <xsl:template match="���������">
            <tr>
                <td id="SvPodrazd" colspan="3" style="text-align:center"><b>�������� �� ������������ �������������� ������������ ���� </b> </td>
            </tr>
            <xsl:if test="��������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � �������� ������������ ����</td>
                </tr>
                <xsl:for-each select="��������">
                    <xsl:call-template name="��������"/>                
                </xsl:for-each>
            </xsl:if>
            <xsl:if test="����������">
                <tr>
                    <td colspan="3" style="text-align:center">�������� � ������������������ ������������ ����</td>
                </tr>
                <xsl:for-each select="����������">
                    <xsl:call-template name="����������"/>                
                </xsl:for-each>
            </xsl:if>
        </xsl:template>
        <xsl:template name="��������">
            <tr>
                <td colspan="3" style="text-align:center"><xsl:value-of select="position()"/></td>
            </tr>
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ �������</td>
                    <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                 </tr>
            </xsl:if>
            <xsl:apply-templates select="������"/>
            <xsl:apply-templates select="�������"/>
            <xsl:apply-templates select="�������"/>
            <xsl:apply-templates select="��������������"/>
        </xsl:template>
        <xsl:template name="����������">
            <tr>
                <td colspan="3" style="text-align:center"><xsl:value-of select="position()"/></td>
            </tr>
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ �����������������</td>
                    <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="������"/>
            <xsl:apply-templates select="�������"/>
            <xsl:apply-templates select="�������"/>
            <xsl:apply-templates select="����������������"/>
        </xsl:template>
        <xsl:template match="������">
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>������������</td>
                <td><xsl:value-of select="@��������"/></td>                
            </tr>
        </xsl:template>
        <xsl:template match="�������">
            <tr>
                <td colspan="3" style="text-align:center">����� (����� ������������) �� ���������� ���������� ���������</td>
            </tr>
            <xsl:if test="@������">
                <tr>
                    <td class="num" align="center"></td>
                    <td align="left">������</td>
                    <td align="left"><xsl:value-of select="@������"/></td>
                </tr>   
            </xsl:if>             
            <tr>
                <td class="num" align="center"></td>
                <td align="left">��� �������� ���������� ���������</td>
                <td align="left"><xsl:value-of select="@���������"/> - <xsl:value-of select="������/@���������"/>&#160;<xsl:value-of select="������/@����������"/></td>
            </tr>
            <xsl:if test="@�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td align="left">��� ������ �� �����</td>
                    <td align="left"><xsl:value-of select="@�����������"/></td>
                </tr> 
            </xsl:if>       
            <tr>
                <td class="num" align="center"></td>
                <td align="left">����� (������� � �.�.)</td>
                <td align="left"><xsl:value-of select="�����/@��������"/>&#160;<xsl:value-of select="�����/@���������"/></td>
            </tr>
            <xsl:if test="����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td align="left">���������� ����� (���� � �.�.)</td>
                    <td align="left"><xsl:value-of select="����������/@�������������"/>&#160;<xsl:value-of select="����������/@��������������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="�����">
                <tr>
                    <td class="num" align="center"></td>
                    <td>����� (���� � �.�.)</td>
                    <td><xsl:value-of select="�����/@��������"/>&#160;<xsl:value-of select="�����/@���������"/></td>
                </tr>
                
            </xsl:if>
            <xsl:if test="�����">
                <tr>
                    <td class="num" align="center"></td>
                    <td>����� (��������, �������� � �.�.)</td>
                    <td><xsl:value-of select="�����/@��������"/>&#160;<xsl:value-of select="�����/@���������"/></td>
                </tr>
                
            </xsl:if>
            <xsl:if test="@���">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� (�������� � �.�.)</td>
                    <td><xsl:value-of select="@���"/></td>
                </tr>                
            </xsl:if>
            <xsl:if test="@������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>������ (�������� � �.�.)</td>
                    <td><xsl:value-of select="@������"/></td>
                </tr>
            </xsl:if>
            <xsl:if test="@�����">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� (���� � �.�.)</td>
                    <td><xsl:value-of select="@�����"/></td>
                </tr>   
            </xsl:if>            
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="�������">
            <tr>
                <td colspan="3" style="text-align:center">����� (����� ������������) �� ��������� ���������� ���������� ���������</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">��� ������</td>
                <td align="left"><xsl:value-of select="@����"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">������������ ������</td>
                <td align="left"><xsl:value-of select="@���������"/></td>
            </tr>
            <xsl:if test="@�����">
                <tr>
                    <td class="num" align="center"></td>
                    <td align="left">�����</td>
                    <td align="left"><xsl:value-of select="@�����"/></td>
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="��������������">
            <tr>
                <td colspan="3" style="text-align:center">�������� �� ����� � ��������� ������ �� ����� ���������� �������</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">��� �������/�����������������</td>
                <td align="left"><xsl:value-of select="@���"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">����������</td>
                <td align="left"><xsl:value-of select="@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� � ��������� ������ �� ����� ���������� �������/�����������������</td>
                <td><xsl:value-of select="����/@�����"/> - <xsl:value-of select="����/@������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>
        <xsl:template match="����������������">
            <tr>
                <td colspan="3" style="text-align:center">�������� �� ����� � ��������� ������ �� ����� ���������� �������</td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">��� �������/�����������������</td>
                <td align="left"><xsl:value-of select="@���"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td align="left">����������</td>
                <td align="left"><xsl:value-of select="@����������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>�������� � ��������� ������ �� ����� ���������� �������/�����������������</td>
                <td><xsl:value-of select="����/@�����"/> - <xsl:value-of select="����/@������"/></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr>  
        </xsl:template>        
        <xsl:template name="��������������">
            <tr>
                <td colspan="3" style="text-align:center"></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td style="text-align:left">������� ��������������� ������</td>
                <td><xsl:value-of select="@�����������������"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>����� � ��������������� ��������, ��������� � ������� � ������ � ������������� "�������������� ��������"</td>
                <td><xsl:value-of select="@�����������������"/></td>                
            </tr>
            <xsl:if test="������������������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� � ������� ����, �� ��������� �������� ��������� �������� �������� ��������������</td>
                    <td><xsl:value-of select="������������������/@���������"/> <br/>
                        ������� �<xsl:value-of select="������������������/@�����"/> �� <xsl:value-of select="������������������/@����"/>
                     </td>              
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="��������">
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������ ����������������� ��� ������� � ���������� ���������, ����� ������� ����������� �� ������������ ���������� ����������� �����������</td>
                <td><xsl:value-of select="@����������"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="��������">
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                    <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                </tr>
            </xsl:if>
            <xsl:apply-templates select="����"/>
            <xsl:if test="��������">
                <xsl:apply-templates select="��������"/>
            </xsl:if>
            <xsl:if test="��������">
                <xsl:apply-templates select="��������"/>
            </xsl:if>
            <xsl:if test="��������">
                <xsl:apply-templates select="��������"/>
            </xsl:if>
            <xsl:if test="���������">
                <xsl:apply-templates select="���������"/>
            </xsl:if>
            <xsl:if test="�������">
                <xsl:apply-templates select="�������"/>
            </xsl:if>
        </xsl:template>
        <xsl:template name="��������">
         
        </xsl:template>
        <xsl:template name="��������">          
        </xsl:template>
        <xsl:template name="���������">
        
        </xsl:template>
        <xsl:template name="�������">
            
        </xsl:template>
        <xsl:template name="��������">
            
        </xsl:template>
        <xsl:template name="����������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � ������������� ����������� - �� </td>
            </tr>
            <xsl:apply-templates select="�������������"/>
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                    <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                </tr>
            </xsl:if>         
        </xsl:template>
        <xsl:template name="����������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � ������������� ����������� - �� </td>
            </tr>
            <xsl:apply-templates select="����"/>
            <xsl:apply-templates select="��������"/>
            <xsl:apply-templates select="��������"/>
            <xsl:apply-templates select="���������"/>
            <xsl:apply-templates select="�������"/>
            
            <xsl:if test="�����������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                    <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                </tr>
            </xsl:if>
        </xsl:template>    
        <xsl:template name="�����������">
            <tr>
                <td colspan="3" style="text-align:center">�������� � ����, �������������� ���������� �����, ����������� � ������� ������������  </td>
            </tr>
            <tr>
                 <td class="num" align="center"></td>
                 <td>���� �������� ���������� (���� ������ ���������)</td>
                 <td><xsl:value-of select="@������������"/></td>                
             </tr>
             <xsl:apply-templates select="����"/>
             <xsl:apply-templates select="��������"/>
             <xsl:apply-templates select="��������"/>
             <xsl:apply-templates select="���������"/>
             <xsl:apply-templates select="�������"/>
             <xsl:if test="�����������">
                 <tr>
                     <td class="num" align="center"></td>
                     <td>��� � ���� �������� � ����� �������� � ������ ����</td>
                     <td><xsl:value-of select="�����������/@���"/><br/><xsl:value-of select="�����������/@����������"/></td>
                 </tr>
             </xsl:if>
        </xsl:template>
        <xsl:template name="�������������">
            <xsl:if test="@����">
               <tr>
                    <td class="num" align="center"></td>
                    <td>�������� ��������������� ��������������� ����� ������������ ����</td>
                    <td><xsl:value-of select="@����"/></td>                
                </tr> 
            </xsl:if>
            <xsl:if test="@���">
                <tr>
                    <td class="num" align="center"></td>
                    <td>��� ������������ ����</td>
                    <td><xsl:value-of select="@���"/></td>                
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>������ ������������ ������������ ����</td>
                <td><xsl:value-of select="@����������"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="���������������">
            <tr>
                <td colspan="3" style="text-align:center"></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>style="text-align:left">������� ��������������� ������</td>
                <td><xsl:value-of select="@������������������"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>����� � ��������������� ��������, ��������� � ������� � ������ � ������������� "�������������� ��������"</td>
                <td><xsl:value-of select="@������������������"/></td>                
            </tr>
            <xsl:if test="�������������������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� � ������� ����, �� ��������� �������� ��������� �������� �������� ��������������</td>
                    <td><xsl:value-of select="�������������������/@���������"/> <br/>
                        ������� �<xsl:value-of select="�������������������/@�����"/> �� <xsl:value-of select="�������������������/@����"/>
                    </td>              
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
            
        </xsl:template>
        <xsl:template name="�������"> 
            <tr>
                <td class="num" align="center"></td>
                <td>���� ������ ���������������</td>
                <td><xsl:value-of select="@������������"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���� ��������� ���������������</td>
                <td><xsl:value-of select="@��������������"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>���� ��������� �������� ������� ������������� � ��������������� </td>
                <td><xsl:value-of select="@�������"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
        <xsl:template name="�����������">
            <tr>
                <td colspan="3" style="text-align:center"></td>
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>style="text-align:left">������� ��������������� ������</td>
                <td><xsl:value-of select="@��������������"/></td>                
            </tr>
            <tr>
                <td class="num" align="center"></td>
                <td>����� � ��������������� ��������, ��������� � ������� � ������ � ������������� "�������������� ��������"</td>
                <td><xsl:value-of select="@��������������"/></td>                
            </tr>
            <xsl:if test="���������������">
                <tr>
                    <td class="num" align="center"></td>
                    <td>�������� � ������� ����, �� ��������� �������� ��������� �������� �������� ��������������</td>
                    <td><xsl:value-of select="���������������/@���������"/> <br/>
                        ������� �<xsl:value-of select="���������������/@�����"/> �� <xsl:value-of select="���������������/@����"/>
                    </td>              
                </tr>
            </xsl:if>
            <tr>
                <td class="num" align="center"></td>
                <td>��� � ���� �������� � ����� ������, ���������� ��������� ��������</td>
                <td><xsl:value-of select="�������/@���"/><br/><xsl:value-of select="�������/@����������"/></td>
            </tr> 
        </xsl:template>
</xsl:stylesheet>