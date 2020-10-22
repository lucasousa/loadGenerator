-- Table: public.workload

-- DROP TABLE public.workload;

CREATE TABLE public.workload
(
  id serial NOT NULL,
  dado bytea,
  CONSTRAINT workload_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.workload
  OWNER TO jederilson;

--Comando para criar a tabela
--psql -h localhost -U jederilson -d testecarga < tablePostgres.sql
