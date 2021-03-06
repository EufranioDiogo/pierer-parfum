PGDMP         4        	        z            sm_db    10.16    10.16 4    R           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            S           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            T           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            U           1262    50682    sm_db    DATABASE     w   CREATE DATABASE sm_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
    DROP DATABASE sm_db;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            V           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12961    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            W           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            ?            1259    58876    account    TABLE     ?   CREATE TABLE public.account (
    account_pk integer NOT NULL,
    username character varying NOT NULL,
    email character varying NOT NULL,
    password character varying NOT NULL
);
    DROP TABLE public.account;
       public         postgres    false    3            ?            1259    58874    account_account_pk_seq    SEQUENCE     ?   CREATE SEQUENCE public.account_account_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.account_account_pk_seq;
       public       postgres    false    206    3            X           0    0    account_account_pk_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.account_account_pk_seq OWNED BY public.account.account_pk;
            public       postgres    false    205            ?            1259    50750 
   buy_orders    TABLE     !  CREATE TABLE public.buy_orders (
    product_fk integer NOT NULL,
    account_fk integer NOT NULL,
    quant_products integer NOT NULL,
    price_per_product double precision NOT NULL,
    total_price double precision NOT NULL,
    date date NOT NULL,
    buy_order_pk integer NOT NULL
);
    DROP TABLE public.buy_orders;
       public         postgres    false    3            ?            1259    93009    buy_orders_buy_order_pk_seq    SEQUENCE     ?   CREATE SEQUENCE public.buy_orders_buy_order_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.buy_orders_buy_order_pk_seq;
       public       postgres    false    204    3            Y           0    0    buy_orders_buy_order_pk_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.buy_orders_buy_order_pk_seq OWNED BY public.buy_orders.buy_order_pk;
            public       postgres    false    207            ?            1259    50707    family    TABLE     k   CREATE TABLE public.family (
    family_pk integer NOT NULL,
    family_name character varying NOT NULL
);
    DROP TABLE public.family;
       public         postgres    false    3            ?            1259    50705    family_family_pk_seq    SEQUENCE     ?   CREATE SEQUENCE public.family_family_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.family_family_pk_seq;
       public       postgres    false    201    3            Z           0    0    family_family_pk_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.family_family_pk_seq OWNED BY public.family.family_pk;
            public       postgres    false    200            ?            1259    50696    origem    TABLE     k   CREATE TABLE public.origem (
    origem_pk integer NOT NULL,
    origem_name character varying NOT NULL
);
    DROP TABLE public.origem;
       public         postgres    false    3            ?            1259    50718    product    TABLE     9  CREATE TABLE public.product (
    product_pk integer NOT NULL,
    name character varying NOT NULL,
    origem_fk integer NOT NULL,
    family_fk integer NOT NULL,
    fragance_rate integer NOT NULL,
    gender character(1) NOT NULL,
    price numeric DEFAULT 0.0 NOT NULL,
    product_photo character varying
);
    DROP TABLE public.product;
       public         postgres    false    3            ?            1259    50694    product_origem_pk_seq    SEQUENCE     ?   CREATE SEQUENCE public.product_origem_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.product_origem_pk_seq;
       public       postgres    false    199    3            [           0    0    product_origem_pk_seq    SEQUENCE OWNED BY     N   ALTER SEQUENCE public.product_origem_pk_seq OWNED BY public.origem.origem_pk;
            public       postgres    false    198            ?            1259    50716    product_product_pk_seq    SEQUENCE     ?   CREATE SEQUENCE public.product_product_pk_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.product_product_pk_seq;
       public       postgres    false    3    203            \           0    0    product_product_pk_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.product_product_pk_seq OWNED BY public.product.product_pk;
            public       postgres    false    202            ?            1259    50685    quoter    TABLE     ?   CREATE TABLE public.quoter (
    quoter_pk integer NOT NULL,
    name character varying(200) NOT NULL,
    quote text NOT NULL,
    photo_url character varying NOT NULL
);
    DROP TABLE public.quoter;
       public         postgres    false    3            ?            1259    50683    quoter_quoter_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.quoter_quoter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.quoter_quoter_id_seq;
       public       postgres    false    197    3            ]           0    0    quoter_quoter_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.quoter_quoter_id_seq OWNED BY public.quoter.quoter_pk;
            public       postgres    false    196            ?
           2604    58879    account account_pk    DEFAULT     x   ALTER TABLE ONLY public.account ALTER COLUMN account_pk SET DEFAULT nextval('public.account_account_pk_seq'::regclass);
 A   ALTER TABLE public.account ALTER COLUMN account_pk DROP DEFAULT;
       public       postgres    false    205    206    206            ?
           2604    93011    buy_orders buy_order_pk    DEFAULT     ?   ALTER TABLE ONLY public.buy_orders ALTER COLUMN buy_order_pk SET DEFAULT nextval('public.buy_orders_buy_order_pk_seq'::regclass);
 F   ALTER TABLE public.buy_orders ALTER COLUMN buy_order_pk DROP DEFAULT;
       public       postgres    false    207    204            ?
           2604    50710    family family_pk    DEFAULT     t   ALTER TABLE ONLY public.family ALTER COLUMN family_pk SET DEFAULT nextval('public.family_family_pk_seq'::regclass);
 ?   ALTER TABLE public.family ALTER COLUMN family_pk DROP DEFAULT;
       public       postgres    false    201    200    201            ?
           2604    50699    origem origem_pk    DEFAULT     u   ALTER TABLE ONLY public.origem ALTER COLUMN origem_pk SET DEFAULT nextval('public.product_origem_pk_seq'::regclass);
 ?   ALTER TABLE public.origem ALTER COLUMN origem_pk DROP DEFAULT;
       public       postgres    false    199    198    199            ?
           2604    50721    product product_pk    DEFAULT     x   ALTER TABLE ONLY public.product ALTER COLUMN product_pk SET DEFAULT nextval('public.product_product_pk_seq'::regclass);
 A   ALTER TABLE public.product ALTER COLUMN product_pk DROP DEFAULT;
       public       postgres    false    203    202    203            ?
           2604    50688    quoter quoter_pk    DEFAULT     t   ALTER TABLE ONLY public.quoter ALTER COLUMN quoter_pk SET DEFAULT nextval('public.quoter_quoter_id_seq'::regclass);
 ?   ALTER TABLE public.quoter ALTER COLUMN quoter_pk DROP DEFAULT;
       public       postgres    false    196    197    197            N          0    58876    account 
   TABLE DATA               H   COPY public.account (account_pk, username, email, password) FROM stdin;
    public       postgres    false    206   ?7       L          0    50750 
   buy_orders 
   TABLE DATA               ?   COPY public.buy_orders (product_fk, account_fk, quant_products, price_per_product, total_price, date, buy_order_pk) FROM stdin;
    public       postgres    false    204   ?:       I          0    50707    family 
   TABLE DATA               8   COPY public.family (family_pk, family_name) FROM stdin;
    public       postgres    false    201   s;       G          0    50696    origem 
   TABLE DATA               8   COPY public.origem (origem_pk, origem_name) FROM stdin;
    public       postgres    false    199   ?;       K          0    50718    product 
   TABLE DATA               v   COPY public.product (product_pk, name, origem_fk, family_fk, fragance_rate, gender, price, product_photo) FROM stdin;
    public       postgres    false    203   ?;       E          0    50685    quoter 
   TABLE DATA               C   COPY public.quoter (quoter_pk, name, quote, photo_url) FROM stdin;
    public       postgres    false    197   ?=       ^           0    0    account_account_pk_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.account_account_pk_seq', 17, true);
            public       postgres    false    205            _           0    0    buy_orders_buy_order_pk_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.buy_orders_buy_order_pk_seq', 13, true);
            public       postgres    false    207            `           0    0    family_family_pk_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.family_family_pk_seq', 5, true);
            public       postgres    false    200            a           0    0    product_origem_pk_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.product_origem_pk_seq', 5, true);
            public       postgres    false    198            b           0    0    product_product_pk_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.product_product_pk_seq', 13, true);
            public       postgres    false    202            c           0    0    quoter_quoter_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.quoter_quoter_id_seq', 9, true);
            public       postgres    false    196            ?
           2606    58884    account account_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_pkey PRIMARY KEY (account_pk);
 >   ALTER TABLE ONLY public.account DROP CONSTRAINT account_pkey;
       public         postgres    false    206            ?
           2606    93016    buy_orders buy_orders_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.buy_orders
    ADD CONSTRAINT buy_orders_pkey PRIMARY KEY (buy_order_pk);
 D   ALTER TABLE ONLY public.buy_orders DROP CONSTRAINT buy_orders_pkey;
       public         postgres    false    204            ?
           2606    50715    family family_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.family
    ADD CONSTRAINT family_pkey PRIMARY KEY (family_pk);
 <   ALTER TABLE ONLY public.family DROP CONSTRAINT family_pkey;
       public         postgres    false    201            ?
           2606    50704    origem product_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.origem
    ADD CONSTRAINT product_pkey PRIMARY KEY (origem_pk);
 =   ALTER TABLE ONLY public.origem DROP CONSTRAINT product_pkey;
       public         postgres    false    199            ?
           2606    50726    product product_pkey1 
   CONSTRAINT     [   ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey1 PRIMARY KEY (product_pk);
 ?   ALTER TABLE ONLY public.product DROP CONSTRAINT product_pkey1;
       public         postgres    false    203            ?
           2606    50693    quoter quoter_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.quoter
    ADD CONSTRAINT quoter_pkey PRIMARY KEY (quoter_pk);
 <   ALTER TABLE ONLY public.quoter DROP CONSTRAINT quoter_pkey;
       public         postgres    false    197            ?
           2606    50727    product family_fk    FK CONSTRAINT     z   ALTER TABLE ONLY public.product
    ADD CONSTRAINT family_fk FOREIGN KEY (family_fk) REFERENCES public.family(family_pk);
 ;   ALTER TABLE ONLY public.product DROP CONSTRAINT family_fk;
       public       postgres    false    2754    201    203            ?
           2606    50732    product origem_fk    FK CONSTRAINT     ?   ALTER TABLE ONLY public.product
    ADD CONSTRAINT origem_fk FOREIGN KEY (origem_fk) REFERENCES public.origem(origem_pk) ON UPDATE CASCADE ON DELETE CASCADE;
 ;   ALTER TABLE ONLY public.product DROP CONSTRAINT origem_fk;
       public       postgres    false    199    203    2752            N     x???ݎ?6????	DΟxW?ٷ?J????k`?M??߸-?d,?????9gF???e???x?o?????r-꿼\????v?L??T?ꕱ?v[|Ӣ-?nzh??nE?嫈5???0?U_-b???fM?w??_??jh???C??4]O????,*"Ew??}\??M%??0?C됙3??EWkZ?q`??I?P?{~V?vq/읙#?????<y??A??A~?ae??&???;??v?K?9???Ewnv?P???To ?eA??????>'??q?c?ɠ+w-?Z@??w>?V?J#W"G???d???????̎??rDf?3߭?????????? ??+1?ߢ??un~Ǉ?`?g???,9N?u?֒G?p/|!Gő???5D?u??S????߇G?"݄"??|?̗?4??f??|?G??Ke?*?"???HR1??钌??u?l ?*~}?K??????????"#Wܰ?c?????u͂AV(????i~3ʄ???$FJ݉u?D????!m???5	v????L?~????M	?i[?{s????䟄????W?rWD?~??$|?Iu?<eR?a?QѨ????ȩ?i????P?? ???A?NE1t??<R??????:????&???Ų\(?0ds???zr[??d????8???k?ӯ??Wb#8Y?	??t
??^?@V?? 5vѣ??	N
?Ck?Y???r??U?{?(:??^Ͽ??????????TlZ?????X??~}??e?~?????N??p???      L   e   x?}???0߰K*LJHw??s?O?A???? 9???lSQ4h?? ? uK?]T??&u??p??5??{?g???,uz?s?^,??????{1?T?=\      I   )   x?3???/M-?2?tʬJ?2rKJ??L9??3??b???? ??      G   4   x?3?.=?293?˘ӭ(1???D.N?Ң??<.SN?Ԝ???D?=... N@?      K   ?  x???ˎ?0???S?iv?]	UMGi?f?VI??1`????O_?y????????????@?j?An?/?il????8?8¨?????jU??ٞ??9?*s.???W????8?DSP+J??(?s*ݧr??4??"???<?5?q?򙺇??mǿ?q???jGG?}=?&͡O~?U?\.n{??ai???]?զ_?????=-/??\??^H???L?YD?5"?vJ??_{?\?@[	??3??+?]WY?@z<??ȧ????_?G??7~?ؔ??7?K Xp?OdH??????????_??v?&?????&?)??5`&@)??C????TI6S?x?`???`?3`^?!z? gr??2?U.XFyJ?ѿl??ߢk~?'~?Ȍ1?/??B?R??P???m??c hS?&O?ނ?ͳP?i*??B????r?-?e??ӂ??`?`ߙ??? ?4fTI F4???S?2??H	?٦??m?-?????      E   ?  x???=r?@?k??TY??,)N?$M??d&E?40	J????.WqtO
O??bEE?
??<?????????ͣe?,kI????B??yj?)?C????+??H???ɓ???S [K?\L[Ǌ,??? ?M?M]??f4b?k
CGT?????Fj	?e?H??QW??A?:Z??C???_T١m?	?1?#>?_?K?魷H?{?:?縓
?O?#8/[b0???n?pz??d???0Dӕ???o?[Q:?2?du?X???H?5?*?{?Ó?#?2?#E??n؈?>[?>?? J?iT??e?'lK??G????F8?PM?W=???|????i:???? ?fK??z)b^?ؓ????Ft`??\?ɗhs?2B??ԡ}?c4?op?{~?????gЍ$?ҹ]E?f?u?w?????J?????UA?o?70?axً?x>Y?V?^????d?????:S??ݹ?|6?o??|???M???ޏa???7~C,     