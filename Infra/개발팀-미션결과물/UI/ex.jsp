<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    // request로 매개변수를 받아옴
    // 모두 String으로 받는다고 함
    String param = request.getParameter("param");
%>
<html>
    <head>
        <title>커피 점수 예측</title>
        <meta charset="utf-8" />
    </head>

    <body>
        <h2>커피 점수 예측</h2>
        <h3>이 커피의 점수는 <%=param%>점입니다.</h3>
        <form action="./">
            <input type="submit" value="초기 화면으로">
        </form>
    </body>
</html>