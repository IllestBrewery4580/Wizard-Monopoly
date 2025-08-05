import pygame
import sys
from game_state import GameState

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH<HEIGHT))
pygame.display.set_caption("ChronoSorcerers: A Monopoly of Magic and Time")

# Set up the clock
clock = pygame.time.Clock()
FPS = 60

# Fonts
font = pygame.font.SysFont(None, 48)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Load board image
board_image = pygame.image.load("assets/board.png")
board_image = pygame.transform.scale(board_image, (WIDTH, HEIGHT))

# Token drawing
def draw_players(game):
    for i, player in enumerate(game.players):
        x = 50 + player.position * 100
        y = 600 + (i * 30)
        pygame.draw.circle(screen, player.color, (x, y), 15)

# --- Name Input Screen ---
def get_player_name():
    input_active = True
    user_text = ""

    while input_active:
        screen.fill(BLACK)
        prompt = font.render("Enter your name:", True, WHITE)
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 - 100))

        input_surface = font.render(user_text, True, WHITE)
        pygame.draw.rect(screen, WHITE< (WIDTH // 2 - 200, HEIGHT // 2 - 40, 400, 60), 2)
        screen.blit(input_surface, (WIDTH // 2 - 190, HEIGHT // 2 - 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user_text.strip() != "":
                    return user_text.strip()
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

            pygame.display.flip()
            clock.tick(FPS)

# Game loop
def main():
    # Step 1: Get player's name
    player_name = get_player_name()

    # Step 2: Set up game
    game = GameState()
    game.add_player(player_name, RED)
    game.add_player("AI Wizard", BLUE)

    current_roll = 0
    show_roll = False
    roll_timer = 0
    ROLL_DISPLAY_TIME = 60     # frames

    while True:
        screen.fill(BLACK)
        screen.blit(board_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Press SPACE to roll dice
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player = game.players[game.current_turn]

                    if player.in_wizard_realm:
                        player.wizard_turns_remaining -= 1
                        if player.wizard_turns_remaining <= 0:
                            player.in_wizard_realm = False
                            print(f"{player.name} escaped the Wizard Realm!")
                        else:
                            current_roll = random.randint(1, 6)
                            player.move(current_roll, len(game.tiles))
                            print(F"{player.name} rolled a {current_roll} and moved to tile {player.position}")
                            game.handle_tile(player)

                        game.next_turn()
                        show_roll = True
                        roll_timer = ROLL_DISPLAY_TIME

        # Show dice roll temporarily
        if show_roll:
            roll_text = font.render(f"Rolled: {current_roll}", True, WHITE)
            screen.blit(roll_text, (WIDTH // 2 - roll_text.get_width() // 2, 50))
            roll_timer -= 1
            if roll_timer <= 0:
                show_roll = False

        draw_players(game)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
