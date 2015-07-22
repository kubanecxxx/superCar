#include "ch.h"
#include "hal.h"
#include "motor.h"

static SerialDriver * dr = &SD1;
static const SerialConfig sdc =
{ 9600, 0, 0, 0 };

void serial_init(void)
{
	palSetPadMode(UART_RX_PORT, UART_RX_PIN, UART_RX_MODE);
	palSetPadMode(UART_TX_PORT, UART_TX_PIN, UART_TX_MODE);
	sdStart(dr, &sdc);
}

void serial_loop(void)
{
	static uint8_t machine = 0;
	static uint8_t data[6];
	static uint8_t idx = 0;
	uint8_t i;

	if (sdGetWouldBlock(dr))
		return;

	uint8_t c = sdGet(dr);

	//decode header and setup speed
	switch (machine)
	{
	case 0:
		idx = 0;
		if (c == 0xfd)
			machine++;
		break;
	case 1:
		if (c == 0xef)
			machine++;
		else
			machine = 0;
		break;
	case 2:
		data[idx++] = c;
		if (idx >= 6)
		{
			idx = 0;
			machine = 3;
		}
		break;
	}

	uint8_t dir;
	uint16_t speed;

	if (machine == 3)
	{
		machine = 0;
		idx = 0;

		for (i = 0 ; i < 2; i++)
		{
			dir = data[i*3];
			speed = data[i*3 + 2];
			speed |= data[i*3 + 1] << 8;
			motor_config(i,dir,speed);
		}
	}
}

