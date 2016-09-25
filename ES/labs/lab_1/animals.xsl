<?xml version="1.0" encoding="UTF-8" ?>
<xsl:stylesheet version="1.0" 
		xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
		xmlns="http://www.w3.org/1999/xhtml">
	<xsl:output method="xml" indent="yes"
		doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" 
		doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"/>
	<xsl:template match="/">
		<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
			<head>
				<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
				<title>Animals</title>
				<link rel="stylesheet" href="./animals.css"/>
			</head>
			<body>
				<h1>
					List of animals 
				</h1>
				<xsl:apply-templates/>
			</body>
		</html>
	</xsl:template>

	<xsl:template match="animals">
		<table>
			<tr><th>#</th><th>Animal</th><th>Skin</th><th>Noise</th><th>Eyes</th></tr>
			<xsl:apply-templates/>
		</table>
	</xsl:template>

	<xsl:template match="animal">
		<tr class="row">
			<td><xsl:number/></td>
			<td><xsl:value-of select="@name"/></td>
			<td><xsl:value-of select="skin"/></td>
			<td><xsl:value-of select="noise"/></td>
			<td><xsl:value-of select="eyes"/></td>
		</tr>
	</xsl:template>
</xsl:stylesheet>