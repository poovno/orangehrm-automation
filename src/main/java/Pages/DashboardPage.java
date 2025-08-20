
package Pages; 
import org.openqa.selenium.By; 
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement; 
import org.openqa.selenium.support.ui.ExpectedConditions; 
import org.openqa.selenium.support.ui.WebDriverWait; 
import java.time.Duration;

public class DashboardPage {
    WebDriver driver;
    WebDriverWait wait;

    By pimMenu = By.xpath("//a[@href='/web/index.php/pim/viewPimModule']");
    By userDropdown = By.cssSelector(".oxd-userdropdown-tab");
    By logoutButton = By.xpath("//a[text()='Logout']");

    public DashboardPage(WebDriver driver) {
        this.driver = driver;
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    public void goToPIM() {
        WebElement pimLink = wait.until(ExpectedConditions.elementToBeClickable(pimMenu));
        pimLink.click();
    }

    public void logout() {
        WebElement dropdown = wait.until(ExpectedConditions.elementToBeClickable(userDropdown));
        dropdown.click();

        WebElement logout = wait.until(ExpectedConditions.elementToBeClickable(logoutButton));
        logout.click();
    }
}

