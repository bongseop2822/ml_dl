# bsgo ���񽺸� ���� ������ �����͸� �����ϴ� ���̺�
# ���� �������� ���̸� �н������� ���ȴ�

CREATE TABLE `tbl_trans_lang_log` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`oCode` VARCHAR(4) NULL DEFAULT NULL COMMENT '�����ڵ�',
	`tCode` VARCHAR(4) NULL DEFAULT NULL COMMENT '�����������ڵ�',
	`oStr` TEXT NULL DEFAULT NULL COMMENT '����',
	`tStc` TEXT NULL DEFAULT NULL COMMENT '������',
	`regDate` TIMESTAMP NULL DEFAULT current_timestamp(),
	PRIMARY KEY (`id`)
)
ENGINE=InnoDB
;
# ������ �߰�
INSERT INTO `py_db`.`tbl_trans_lang_log` 
  (`oCode`, `tCode`, `oStr`, `tStc`) 
VALUES 
  ('en', 'ko', 'hello', '�ȳ�');