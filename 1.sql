Pragma foreign_keys=false;
Begin Transaction;
Drop Table If Exists [C1_category];
CREATE TABLE "C1_category"(
[id] integer PRIMARY KEY NOT NULL
,[c_name] varchar(20) NOT NULL
,[c_father] integer NOT NULL DEFAULT 0
   
);
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("1","罗莱","0");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("2","优家","0");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("3","宝缦","0");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("4","其他","0");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("5","芯类","1");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("6","家居类","1");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("7","团购类","1");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("8","应季商品","1");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("9","新经典","1");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("10","新优雅","1");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("11","新温馨","1");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("12","新时尚","1");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("13","床垫","5");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("14","被芯","5");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("15","枕芯","5");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("16","靠垫","6");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("17","毯类","6");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("18","毛浴巾","6");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("19","家居服","6");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("20","饰品","6");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("21","芯类","7");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("22","毛浴巾类","7");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("23","毯类","7");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("24","套件类","7");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("25","新特奇类","7");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("26","席类","8");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("27","毯类","8");
Insert  Into [C1_category] ([id],[c_name],[c_father]) Values("28","蚊帐类","8");
Drop Table If Exists [C1_man];
CREATE TABLE "C1_man" (
    "id" integer NOT NULL PRIMARY KEY,
    "sid" varchar(18) NOT NULL,
    "name" varchar(10) NOT NULL,
    "tname" varchar(10) NOT NULL,
    "category" varchar(2) NOT NULL
);
Insert  Into [C1_man] ([id],[sid],[name],[tname],[category]) Values("1","341226198012310216","李先锋","先锋","6");
Insert  Into [C1_man] ([id],[sid],[name],[tname],[category]) Values("2","341226197706010001","汪乩童","汪汪","1");
Drop Table If Exists [C1_celldb];
CREATE TABLE "C1_celldb" (
    "id" integer NOT NULL PRIMARY KEY,
    "number" varchar(11) NOT NULL,
    "owner_id" integer NOT NULL REFERENCES "C1_man" ("id")
);
Insert  Into [C1_celldb] ([id],[number],[owner_id]) Values("1","13966560005","1");
Insert  Into [C1_celldb] ([id],[number],[owner_id]) Values("2","13826201918","1");
Insert  Into [C1_celldb] ([id],[number],[owner_id]) Values("3","13701000001","1");
Insert  Into [C1_celldb] ([id],[number],[owner_id]) Values("4","626700","2");
Commit Transaction;
Pragma foreign_keys=true;
