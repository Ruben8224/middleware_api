INSERT INTO TA_SMS_MAESTRO (id, nombre_campania, fecha_envio) VALUES
(1, 'Campaña Bienvenida', '2025-04-01'),
(2, 'Campaña Promoción Abril', '2025-04-01'),
(3, 'Campaña Encuesta Satisfacción', '2025-04-02'),
(4, 'Campaña Recompensa', '2025-04-02'),
(5, 'Campaña Nuevos Clientes', '2025-04-03'),
(6, 'Campaña Reactivación', '2025-04-03'),
(7, 'Campaña Recordatorio Cita', '2025-04-04'),
(8, 'Campaña Cobranza', '2025-04-04'),
(9, 'Campaña Día del Niño', '2025-04-05'),
(10, 'Campaña Evento Especial', '2025-04-05');


INSERT INTO TA_SMS_DETALLE (id, id_maestro, telefono, mensaje) VALUES
(1, 1, '5551000001', '¡Bienvenido a nuestro servicio!'),
(2, 1, '5551000002', 'Gracias por registrarte.'),
(3, 1, '5551000003', 'Te damos la bienvenida.'),
(4, 1, '5551000004', 'Activación exitosa.'),

(5, 2, '5552000001', 'Aprovecha nuestra promo de abril.'),
(6, 2, '5552000002', 'Solo por hoy: 30% de descuento.'),
(7, 2, '5552000003', 'Última oportunidad de abril.'),
(8, 2, '5552000004', 'Visítanos y gana puntos.'),

(9, 3, '5553000001', 'Ayúdanos con esta encuesta.'),
(10, 3, '5553000002', 'Tu opinión es importante.'),
(11, 3, '5553000003', 'Participa en la encuesta.'),
(12, 3, '5553000004', 'Encuesta de satisfacción.'),

(13, 4, '5554000001', '¡Has ganado un cupón!'),
(14, 4, '5554000002', 'Canjea tu recompensa ahora.'),
(15, 4, '5554000003', 'Gracias por participar.'),
(16, 4, '5554000004', 'Tu premio está disponible.'),

(17, 5, '5555000001', 'Gracias por elegirnos.'),
(18, 5, '5555000002', 'Te damos la bienvenida.'),
(19, 5, '5555000003', 'Eres parte de nuestra comunidad.'),
(20, 5, '5555000004', 'Tu cuenta fue activada.'),

(21, 6, '5556000001', '¡Te extrañamos! Regresa ahora.'),
(22, 6, '5556000002', 'Vuelve y obtén un descuento.'),
(23, 6, '5556000003', 'Reactivamos tu cuenta.'),
(24, 6, '5556000004', 'Último aviso para reactivar.'),

(25, 7, '5557000001', 'Recuerda tu cita el lunes.'),
(26, 7, '5557000002', 'Confirmación de cita.'),
(27, 7, '5557000003', 'Tu cita es mañana.'),
(28, 7, '5557000004', 'Consulta médica programada.'),

(29, 8, '5558000001', 'Tienes un pago pendiente.'),
(30, 8, '5558000002', 'Evita cargos, paga a tiempo.'),
(31, 8, '5558000003', 'Regulariza tu situación.'),
(32, 8, '5558000004', 'Tu factura está vencida.'),

(33, 9, '5559000001', '¡Feliz Día del Niño! 🎉'),
(34, 9, '5559000002', 'Celebra con nosotros.'),
(35, 9, '5559000003', 'Regalamos sonrisas.'),
(36, 9, '5559000004', 'Participa en el sorteo.'),

(37, 10, '5560000001', 'No faltes al evento especial.'),
(38, 10, '5560000002', 'Confirmación de asistencia.'),
(39, 10, '5560000003', 'Te esperamos este sábado.'),
(40, 10, '5560000004', 'Revisa la agenda del evento.');
