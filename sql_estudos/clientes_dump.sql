BEGIN TRANSACTION;
CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
 , bloqueado BOOLEAN);
INSERT INTO "clientes" VALUES(1,'REGIS',35,'45666778998','regis@email.com','11-1000-2014','Sao Paulo','SP','2014-06-07',NULL);
INSERT INTO "clientes" VALUES(3,'Jose',33,'56788897645','jose@email.com','51-97878-5645','Rio grande do sul','RS','2020=09-09',NULL);
INSERT INTO "clientes" VALUES(4,'Fabio',23,'44455566678','fabio@email.com','1234-5678','Belo horizonte','MG','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(5,'joao',55,'57829786756','joao@email.com','11-1234-4321','Sao paulo','SP','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(6,'Xavier',24,'66688899967','xavier@email.com','12-3456-7654','Campinas','SP','2014-07-08',NULL);
INSERT INTO "clientes" VALUES(7,'Vitor',21,'87676556774','vitor@email.com','54-7869-8766','Porto Alegre','RS','2024-11-19',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',7);
COMMIT;
