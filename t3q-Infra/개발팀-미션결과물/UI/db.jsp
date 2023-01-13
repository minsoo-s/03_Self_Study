<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import = "org.json.simple.*" %>
<%@ page import = "org.json.simple.parser.*" %>
<html>

<head>
    <title>History</title>
    <meta charset="utf-8">
</head>

<body>
    <h2>History</h2>
    <table border="1">
        <tr>
            <td width="100">index</td>
            <td width="100">aroma</td>
            <td width="100">flavor</td>
            <td width="100">acidity</td>
            <td width="100">balance</td>
        </tr>
    <%
    try{
        String data_table = request.getParameter("table");
        JSONParser jsonParser = new JSONParser();
        JSONObject jsonObj = (JSONObject)jsonParser.parse(data_table);
        JSONArray InfoArray = (JSONArray)jsonObj.get("info");
    
        for(int i = 0; i < InfoArray.size(); i++){
            JSONObject infoObject = (JSONObject) InfoArray.get(i);

            out.println("<tr>");
            out.println("<td>" + infoObject.get("idx") + "</td>");
            out.println("<td>" + infoObject.get("aroma") + "</td>");
            out.println("<td>" + infoObject.get("flavor") + "</td>");
            out.println("<td>" + infoObject.get("acidity") + "</td>");
            out.println("<td>" + infoObject.get("balance") + "</td>");
            out.println("</tr>");
        }
    } catch (ParseException e) {
        e.printStackTrace();
    }
    %>
    </table>
    <form action="./index.jsp">
        <input type="submit" value="초기 화면으로">
    </form>
</body>
</html>
