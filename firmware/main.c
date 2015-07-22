/*
 ChibiOS/RT - Copyright (C) 2006-2013 Giovanni Di Sirio

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */

#include <uart_prot.h>
#include "ch.h"
#include "hal.h"
#include "scheduler.h"
#include "time.h"
#include "motor.h"


void blik(arg_t v)
{
	(void )v;
	palTogglePad(TEST_LED_PORT,TEST_LED_PIN);
}



/*
 * Application entry point.
 */
systime_t sysTime;

static delay_t s1;

int main(void)
{

	halInit();
	chSysInit();

	//kruciální řádky - odpojit jtag; nechat jenom swd - sou na nem piny pro SPI1
	//premapovat SPI1 na PB3;4;5
	/*
	RCC->APB2ENR |= RCC_APB2ENR_AFIOEN;
	AFIO->MAPR |= AFIO_MAPR_SPI1_REMAP;
	AFIO->MAPR |= 0b010 << 24;
*/

	//blinking diode
	shFillStruct(&s1,blik,NULL,MS2ST(500),PERIODIC);
	shRegisterStruct(&s1);

	palSetPadMode(TEST_LED_PORT, TEST_LED_PIN, PAL_MODE_OUTPUT_PUSHPULL);
	palSetPadMode(TEST_LED_PORT2, TEST_LED_PIN2, PAL_MODE_OUTPUT_PUSHPULL);

	palClearPad(TEST_LED_PORT, TEST_LED_PIN);
	palClearPad(TEST_LED_PORT2, TEST_LED_PIN2);

	serial_init();
	motor_init();

	while (TRUE)
	{
		shPlay();
		sysTime = chTimeNow();
		serial_loop();
	}


}

