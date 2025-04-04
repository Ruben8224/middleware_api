CREATE DATABASE IF NOT EXISTS middleware_db;
USE middleware_db;

CREATE TABLE IF NOT EXISTS TA_SMS_MAESTRO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_campania VARCHAR(255) NOT NULL,
    fecha DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS TA_SMS_DETALLE (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_maestro INT NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    mensaje TEXT NOT NULL,
    FOREIGN KEY (id_maestro) REFERENCES TA_SMS_MAESTRO(id) ON DELETE CASCADE
);

DELIMITER //

CREATE PROCEDURE GetCampaniasPorFecha(IN fecha_busqueda DATE)
BEGIN
    SELECT * FROM TA_SMS_MAESTRO
    WHERE fecha = fecha_busqueda;
END //

CREATE PROCEDURE GetDetallesPorCampania(
    IN id_campania INT,
    IN offset_val INT,
    IN limit_val INT
)
BEGIN
    SELECT id, id_maestro, telefono, mensaje
    FROM TA_SMS_DETALLE
    WHERE id_maestro = id_campania
    LIMIT offset_val, limit_val;
END //

DELIMITER ;

-- Datos de ejemplo
INSERT INTO TA_SMS_MAESTRO (nombre_campania, fecha) VALUES
('Campaña Promocional A', '2020-08-11'),
('Campaña Bienvenida Clientes', '2020-08-11');

INSERT INTO TA_SMS_DETALLE (id_maestro, telefono, mensaje) VALUES
(1, '5551234567', 'Hola, aprovecha nuestra promoción especial A.'),
(1, '5559876543', '¡Últimos días para participar en Campaña A!'),
(2, '5543217890', 'Bienvenido a nuestro servicio, disfruta tu experiencia.');

COMMIT;