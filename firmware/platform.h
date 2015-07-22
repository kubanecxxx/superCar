/**
 * @file platform.h
 * @author kubanec
 * @date 8. 4. 2014
 *
 */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef PLATFORM_H_
#define PLATFORM_H_

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
/* Exported types ------------------------------------------------------------*/
/* Exported constants --------------------------------------------------------*/
/* Exported macro ------------------------------------------------------------*/
/* Exported functions --------------------------------------------------------*/





#define TEST_LED_PORT 	GPIOC
#define TEST_LED_PIN	14
#define TEST_LED_PORT2	GPIOC
#define TEST_LED_PIN2	15



#define UART_RX_PORT	GPIOA
#define UART_TX_PORT	GPIOA
#define UART_RX_PIN		10
#define UART_TX_PIN		9
#define UART_RX_MODE	PAL_MODE_INPUT
#define UART_TX_MODE	PAL_MODE_STM32_ALTERNATE_PUSHPULL




#ifdef __cplusplus
}
#endif

#endif /* PLATFORM_H_ */
