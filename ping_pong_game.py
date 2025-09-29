# ============ Initialization (kutubxonalarni ulash) ===============
import pygame
import sys
# ==================================================================

# ===== Bu joy keraksiz, lekin Initialization bo‘ladi. (O‘yinda ishlatmaymiz).=========
from pygame.examples.go_over_there import screen, running
# ===================================================================================

# ======== Initialization (kutubxonani ishga tushirish) ==================
pygame.init()
# ========================================================================

# ======== Setup (o‘yin oynasi sozlash, boshlang‘ich parametrlar) ==========
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")
# ==========================================================================

# ======== Initialization (doimiy qiymatlar — constants) ===================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
# ==========================================================================

# =================== Initialization (taymer sozlash) ======================
clock = pygame.time.Clock()
FPS = 60
# ==========================================================================

# ========== Initialization (obyekt yaratish — raketka) ====================
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2,
                     HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
# ==========================================================================

# ==== Initialization (obyekt yaratish — to‘p + tezlik parametrlari) =======
BALL_SIZE = 15
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 4
ball_speed_y = -4
# ==========================================================================

# =========== Initialization (hisob va shrift sozlash) =====================
score = 0
font = pygame.font.SysFont("Arial", 24)
# ==========================================================================

# =========== Bu butunlay Operation + Output funksiyasi. ===================
def draw_window():
    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, paddle)

    pygame.draw.ellipse(screen, RED, ball)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
# ==========================================================================

# ============== Bu Loop + Event Handling + Condition. =====================
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# ==========================================================================

    # ========================== Condition + Update. =======================
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 6
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += 6

    # ========================= Update =====================================
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # ======================================================================

    # ========================== Condition + Update. =======================
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    # ======================================================================

    # ========================== Condition + Update. =======================
    if ball.colliderect(paddle):
        ball_speed_y *= -1
        score += 1
    # ======================================================================

    # ============= Condition + Output + Termination =======================
    if ball.bottom >= HEIGHT:
        print("Game Over! Score:", score)
        running = False
    # ======================================================================

    draw_window()     # Operation (funksiya chaqirish)

pygame.quit()         # Termination
sys.exit()            # Termination

# Algoritmlar nazariyasida ishlatiladigan asosiy blok turlari:
#
# Initialization / Setup → boshlang‘ich sozlash (o‘zgaruvchilar, kutubxona chaqirish, resurs tayyorlash).
#
# Input / Output (I/O) → foydalanuvchidan ma’lumot olish yoki ekranga chiqarish.
#
# Operation / Update → hisoblash, o‘zgaruvchilarni yangilash, obyektni harakatlantirish.
#
# Condition (if / elif / else) → qaror qabul qilish, shartni tekshirish.
#
# Loop (for / while) → takrorlash jarayonlari.
#
# Event handling → tashqi hodisaga javob berish (masalan, tugma bosish).
#
# Termination (Exit) → dastur tugashi.



























