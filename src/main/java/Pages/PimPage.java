package Pages;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;

public class PimPage {
    WebDriver driver;
    WebDriverWait wait;

    By addEmployeeBtn = By.xpath("//*[normalize-space(text())='Add Employee']");
    By firstName = By.name("firstName");
    By lastName = By.name("lastName");
    By saveBtn = By.xpath("//button[@type='submit']");
    By employeeList = By.xpath("//*[normalize-space(text())='Employee List']");
    By searchBox = By.xpath("//input[@placeholder='Type for hints...']");
    By searchBtn = By.xpath("//button[@type='submit']");

    public PimPage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    public void addEmployee(String fname, String lname) {
        wait.until(ExpectedConditions.elementToBeClickable(addEmployeeBtn)).click();
        wait.until(ExpectedConditions.visibilityOfElementLocated(firstName)).sendKeys(fname);
        driver.findElement(lastName).sendKeys(lname);
        driver.findElement(saveBtn).click();
    }

    public void searchEmployee(String name) {
        wait.until(ExpectedConditions.elementToBeClickable(employeeList)).click();
        wait.until(ExpectedConditions.visibilityOfElementLocated(searchBox)).sendKeys(name);
        driver.findElement(searchBtn).click();
    }
}
