/*
 * motor.h
 *
 *  Created on: 22. 7. 2015
 *      Author: kuba
 */

#ifndef MOTOR_MOTOR_H_
#define MOTOR_MOTOR_H_

void motor_init(void);
void motor_config(uint8_t motor_idx, uint8_t direction,uint16_t percent);


#endif /* MOTOR_MOTOR_H_ */
