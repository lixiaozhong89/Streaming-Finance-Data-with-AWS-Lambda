{\rtf1\ansi\ansicpg1252\cocoartf2577
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 SELECT b.company AS Company, b.high AS High, b.hour AS Hour, a.ts AS Datetime\
FROM "21" a\
JOIN (SELECT company AS Company, MAX(high) AS High, CAST(SUBSTRING(ts, 12,2) AS int) AS Hour\
FROM "21" \
GROUP BY 1, 3\
ORDER BY 1, 3) b\
ON a.company = b.company \
AND a.high = b.High\
AND CAST(SUBSTRING(a.ts, 12,2) AS int) = b.Hour\
ORDER BY 1, 3;}