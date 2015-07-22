/*
 * motor.c
 *
 *  Created on: 22. 7. 2015
 *      Author: kuba
 */

#include "ch.h"
#include "hal.h"
#include "motor.h"

/*
 * PWM configuration structure.
 * Cyclic callback enabled, channels 3 and 4 enabled without callbacks,
 * the active state is a logic one.
 */
static PWMConfig pwmcfg =
{ 1000000, /* 10kHz PWM clock frequency.   */
10000, /* PWM period 1S (in ticks).    */
NULL,
{
{ PWM_OUTPUT_ACTIVE_HIGH, NULL },
{ PWM_OUTPUT_ACTIVE_HIGH, NULL },
{ PWM_OUTPUT_ACTIVE_HIGH, NULL },
{ PWM_OUTPUT_ACTIVE_HIGH, NULL } },
/* HW dependent part.*/
0, 0,
#if STM32_PWM_USE_ADVANCED
		0
#endif
	};

static PWMDriver * pwm = &PWMD3;

void motor_init(void)
{
	//pin init
	palSetPadMode(GPIOA, 6, PAL_MODE_STM32_ALTERNATE_PUSHPULL);
	palSetPadMode(GPIOA, 7, PAL_MODE_STM32_ALTERNATE_PUSHPULL);
	palSetPadMode(GPIOB, 0, PAL_MODE_STM32_ALTERNATE_PUSHPULL);
	palSetPadMode(GPIOB, 1, PAL_MODE_STM32_ALTERNATE_PUSHPULL);

	pwmStart(pwm, &pwmcfg);

	//pwmEnableChannel(&PWMD2, 2, PWM_PERCENTAGE_TO_WIDTH(&PWMD2, ja));
}

void motor_config(uint8_t idx, uint8_t dir, uint16_t percent)
{
	if (idx > 1)
		return;
	if (dir > 1)
		return;
	if (percent > 10000)
		return;

	uint8_t swap;
	uint8_t ch1 = 0;
	uint8_t ch2 = 1;

	if (idx)
	{
		ch1 = 2;
		ch2 = 3;
	}


	if (dir)
	{
		swap = ch1;
		ch1 = ch2;
		ch2 = swap;
	}

	pwmEnableChannel(pwm, ch1, PWM_PERCENTAGE_TO_WIDTH(pwm, percent));
	pwmEnableChannel(pwm, ch2, PWM_PERCENTAGE_TO_WIDTH(pwm, 0));
}
