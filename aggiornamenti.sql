select max(idanagrafe) from attivita.ae_anagrafe;
CREATE SEQUENCE attivita.ae_anagrafe_idanagrafe_seq MINVALUE 1158;
ALTER TABLE attivita.ae_anagrafe ALTER idanagrafe SET DEFAULT nextval('attivita.ae_anagrafe_idanagrafe_seq');
ALTER SEQUENCE attivita.ae_anagrafe_idanagrafe_seq OWNED BY attivita.ae_anagrafe.idanagrafe;